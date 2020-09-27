import discord
from discord.ext import commands
import os
import psycopg2

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

class MyWarns(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def mwarn(self, ctx, member: discord.Member = None):

        try:
            
            member = ctx.author if not member else member
            guild = ctx.message.guild

            cursor.execute(f'SELECT counts FROM public."Warns" WHERE guild_id = \'{guild.id}\' AND member_id = \'{member.id}\';')
            count = cursor.fetchone()
            conn.commit()
        
            if count is None:
                emb = discord.Embed(
                    title = 'Предупреждения',
                    description = f'У пользователя {member.mention} есть 0 предупреждений',
                    timestamp = ctx.message.created_at,
                    colour = discord.Color.green()
                )
                await ctx.send(embed = emb)
            
            else:
                emb = discord.Embed(
                    title = 'Предупреждения',
                    description = f'У пользователя {member.mention} есть {count[0]} предупреждений',
                    timestamp = ctx.message.created_at,
                    colour = discord.Color.green()
                )
                await ctx.send(embed = emb)
        
        except Exception as e:
            print(f'[{ctx.message.created_at}] [{ctx.message.guild.name}] [{ctx.message.guild.owner}] - [{e}]')
    
    async def cog_command_error(self, ctx: commands.Context, error: commands.CommandError):
        await ctx.send('Произошла ошибка: {}'.format(str(error)))
        print(f'[{ctx.message.created_at}] [{ctx.message.guild.name}] [{ctx.message.guild.owner}] - [{error}]')
        
def setup(bot):
    bot.add_cog(MyWarns(bot))
