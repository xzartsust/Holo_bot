import discord
from discord.ext import commands
import asyncpg
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

class Warns(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def warn(self, ctx, member: discord.Member):

        guild = ctx.message.guild
        member_id = member.id

        print('member id ', member_id)

        cursor.execute(f'SELECT counts FROM public."Warns" WHERE guild_id = \'{guild.id}\' AND member_id = \'{member_id}\';')
        count = cursor.fetchone()
        conn.commit()

        print('Warns ', count[0])


def setup(bot):
    bot.add_cog(Warns(bot))