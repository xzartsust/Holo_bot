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

class WelcomeTextTitle(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def wtext(self, ctx, *, title: str = None):

        guild = ctx.message.guild
        if title is not None:
            cursor.execute(f'UPDATE public."Texts_For_Welcome" SET title = \'{title}\' WHERE guild_id = \'{guild.id}\';')
            conn.commit()
        else:
            cursor.execute(f'UPDATE public."Texts_For_Welcome" SET title = Null WHERE guild_id = \'{guild.id}\';')
            conn.commit()

def setup(bot):
    bot.add_cog(WelcomeTextTitle(bot))