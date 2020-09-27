import discord
from discord.ext import commands
import os
import psycopg2
import asyncio, asyncpg

database = os.environ.get('DATABASE')
user = os.environ.get('USER')
password = os.environ.get('PASSWORD')
host = os.environ.get('HOST')
port = os.environ.get('PORT')

conn = psycopg2.connect(
    database = f"{database}", 
    user = f"{user}", 
    password = f"{password}", 
    host = f"{host}", 
    port = "5432"
)

cursor = conn.cursor()

class UnMute(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members = True)
    async def unmute(self, ctx, who: discord.Member):
        
        guild = ctx.message.guild

        try:
         
            cursor.execute(f'SELECT role_for_mute FROM public."myBD" WHERE guild_id = \'{guild.id}\';')
            role_mute = cursor.fetchone()
            conn.commit()
            role = ctx.message.guild.get_role(role_mute[0])
        
            await ctx.channel.purge(limit = 1)

            unmute = discord.Embed(
                title = f'З {who} был снят мут',
                timestamp = ctx.message.created_at,
                colour = discord.Color.green()
                )
            unmute.add_field(
                name = 'Пользователь',
                value = f'{who.mention}'
                )
            unmute.add_field(
                name = 'Модератор',
                value = f'{ctx.message.author.mention}'
                )
            await ctx.send(embed = unmute)
            
            await who.remove_roles(role)
        
        except Exception as e:
            print(f'[{ctx.message.created_at}] [{ctx.message.guild.name}] [{ctx.message.guild.owner}] - [{e}]')

    async def cog_command_error(self, ctx: commands.Context, error: commands.CommandError):
        await ctx.send('Произошла ошибка: {}'.format(str(error)))
        print(f'[{ctx.message.created_at}] [{ctx.message.guild.name}] [{ctx.message.guild.owner}] - [{error}]')



def setup(bot):
    bot.add_cog(UnMute(bot))