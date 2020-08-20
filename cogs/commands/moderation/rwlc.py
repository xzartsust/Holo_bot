import discord
from discord.ext import commands
import os
import asyncpg, asyncio
import psycopg2

####################################################################################################################

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


####################################################################################################################

def is_owner_guild(ctx):
    return ctx.author.id == ctx.guild.owner.id

class AuthoAddRole(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, guild):

        cursor.execute(f'SELECT on_or_off FROM public."giveroles" WHERE guild_id = {guild.id};')
        on_or_off = cursor.fetchone()
        conn.commit()

        cursor.execute(f'SELECT role_id FROM public."giveroles" WHERE guild_id = {guild.id};')
        role = cursor.fetchone()
        conn.commit()
        
        print(on_or_off[0])
        print(role[0])


    @commands.command()
    @commands.check(is_owner_guild)
    async def rwlc(self, ctx, role, types):
        guild = ctx.message.guild

        cursor.execute(f'UPDATE public."giveroles" SET role_id = \'{role}\' WHERE guild_id = \'{guild.id}\';')
        conn.commit()

        cursor.execute(f'UPDATE public."giveroles" SET on_or_off = \'{types}\' WHERE guild_id = \'{guild.id}\';')
        conn.commit()

        await ctx.send('ok')



def setup(bot):
    bot.add_cog(AuthoAddRole(bot))