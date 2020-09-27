import discord
from discord.ext import commands
import asyncpg, asyncio
import psycopg2
import os

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

class bot_join_guild(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        
        try:
            cursor.execute(f'DELETE FROM public."myBD" WHERE guild_id = \'{guild.id}\';')
            conn.commit()

            cursor.execute(f'DELETE FROM public."Texts_For_Welcome" WHERE guild_id = \'{guild.id}\';')
            conn.commit()

            cursor.execute(f'DELETE FROM public."Warns" WHERE guild_id = \'{guild.id}\';')
            conn.commit()
        
        except Exception as e:
            print(f'[{guild.name}] [{guild.owner}] - [{e}]')

def setup(bot):
    bot.add_cog(bot_join_guild(bot))