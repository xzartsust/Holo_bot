import discord
from discord.ext import commands
import os
import asyncpg, asyncio
import psycopg2
from discord import utils
from discord.utils import get


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


class ServerInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    

    @commands.command(aliases = ['si','is'])
    async def serverinfo(self, ctx):
        pass


def setup(bot):
    bot.add_cog(ServerInfo(bot))