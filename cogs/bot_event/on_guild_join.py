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
    async def on_guild_join(self, guild): 
        cursor.execute(f'INSERT INTO public."prefixDB" (guild_id, prefix) VALUES ({guild.id}, \'t!\');')
        conn.commit()
        cursor.execute(f'INSERT INTO public.giveroles(guild_id, on_or_off) VALUES ({guild.id}, false);')
        conn.commit()
        
def setup(bot):
    bot.add_cog(bot_join_guild(bot))