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
        join_guild_id = guild.id
        cursor.execute(f'INSERT INTO public."prefixDB"(guild_id, prefix) VALUES ({join_guild_id},".");')
        conn.commit()

    @commands.Cog.listener()
    async def on_guild_remove(self,guild):
        pass
        '''remove_guild_id = guild.id
        remove_guild_prefix = cursor.execute()
        cursor.execute(f'DELETE FROM public."prefixDB" WHERE guild_id = "{remove_guild_id}" AND prefix = {remove_guild_prefix};')
        conn.commit()'''

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def prefix(self, ctx):
        cursor.execute('INSERT INTO public."prefixDB"(guild_id, prefix)	VALUES (12,12);')
        conn.commit()


def setup(bot):
    bot.add_cog(prefix(bot))

