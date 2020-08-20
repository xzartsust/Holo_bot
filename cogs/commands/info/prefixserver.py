import discord
from discord.ext import commands
import os
import asyncio, asyncpg
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

################################################################################################################################

class PrefixServer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ['ps','sp'])
    async def prefixserver(self, ctx):
        guild = ctx.message.guild

        cursor.execute(f'SELECT prefix FROM public."prefixDB" WHERE guild_id = \'{guild.id}\';')
        prefix = cursor.fetchone()

        await ctx.send(f'Server Prefix: \"**{prefix[0]}**\"')

def setup(bot):
    bot.add_cog(PrefixServer(bot))