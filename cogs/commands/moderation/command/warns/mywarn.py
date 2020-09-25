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
    @commands.is_owner()
    async def mwarn(self, ctx):
        
        user = ctx.message.author.id
        guild = ctx.message.guild

        cursor.execute(f'SELECT counts FROM public."Warns" WHERE guild_id = \'{guild.id}\' AND member_id = \'{user}\';')
        count = cursor.fetchone()
        conn.commit()
        
        if count is None:
            print('0')
        else:
            print(count[0])

def setup(bot):
    bot.add_cog(MyWarns(bot))