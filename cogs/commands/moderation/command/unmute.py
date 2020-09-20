import discord
from discord.ext import commands
import os
import psycopg2
import asyncio, asyncpg

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

class UnMute(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command
    @commands.has_permissions(kick_members = True)
    async def unmute(self, ctx, who: discord.Member):
        
        guild = ctx.message.guild
        cursor.execute(f'SELECT role_for_mute FROM public."myBD" WHERE guild_id = \'{guild.id}\';')
        role_mute = cursor.fetchone()
        conn.commit()
        role = ctx.message.guild.get_role(role_mute[0])
        
        await ctx.channel.purge(limit = 1)

        await ctx.send(f'С {who} был снят мут')
        await who.remove_roles(role)

def setup(bot):
    bot.add_cog(UnMute(bot))