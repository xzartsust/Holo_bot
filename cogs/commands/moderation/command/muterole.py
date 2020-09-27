import discord
from discord.ext import commands
import os
import asyncio, asyncpg
import psycopg2

########################################################## Connect to SQL ###################################################

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

##############################################################################################################################

def is_owner_guild(ctx):
    return ctx.author.id == ctx.guild.owner.id

class MuteRole(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.check(is_owner_guild)
    async def muterole(self, ctx, role_id: int):
        guild = ctx.message.guild
        role = ctx.message.guild.get_role(role_id)

        try:

            cursor.execute(f'UPDATE public."myBD" SET role_for_mute = \'{role_id}\' WHERE guild_id = \'{guild.id}\';')
            conn.commit()

            emb = discord.Embed(
                title= 'Успешно!',
                description = f'Роль {role.mention} была установленна для команды `mute`',
                timestamp = ctx.message.created_at
                )
            emb.set_footer(
                text = 'Запросил: ' + f'{ctx.author}',
                icon_url = ctx.author.avatar_url
                )
        
            if ctx.guild.system_channel is not None:
                await ctx.guild.system_channel.send(embed = emb)
            elif ctx.guild.system_channel is None:
                await ctx.send(embed = emb)
        
        except Exception as e:
            print(f'[{ctx.message.created_at}] [{ctx.message.guild.name}] [{ctx.message.guild.owner}] - [{e}]')
    
    async def cog_command_error(self, ctx: commands.Context, error: commands.CommandError):
        await ctx.send('Произошла ошибка: {}'.format(str(error)))
        print(f'[{ctx.message.created_at}] [{ctx.message.guild.name}] [{ctx.message.guild.owner}] - [{error}]')

def setup(bot):
    bot.add_cog(MuteRole(bot))