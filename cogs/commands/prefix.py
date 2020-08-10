import discord
from discord.ext import commands
import os
import asyncpg, asyncio
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

PREFIX=('.')

class prefix(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        pass
        

    @commands.Cog.listener()
    async def on_guild_remove(self,ctx):
        pass


    @commands.command()
    @commands.has_permissions(administrator=True)
    async def prefix(self, ctx):
        cursor.execute('INSERT INTO public."prefixDB"(guild_id, prefix)	VALUES ({},{});').format(12,13)


def setup(bot):
    bot.add_cog(prefix(bot))

