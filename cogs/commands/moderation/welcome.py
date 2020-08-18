import discord
from discord.ext import commands
import asyncpg, asyncio
import psycopg2
import os
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

class member_greeting(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        join_guild_id = member.guild.id
        cursor.execute(f'SELECT channel_for_greeting FROM public."prefixDB" WHERE guild_id = \'{join_guild_id}\';')
        chan = cursor.fetchone()
        conn.commit()
        channel = self.bot.get_channel(chan[0])

        emb = discord.Embed(
            title = 'Поприветствуем нового члена нашего сервера',
            description = f'Привет {member}'
            timestamp = member.message.created_at
        )

        await channel.send(embed = emb)
    
    @commands.command(aliases=['wlc'])
    async def welcome(self, ctx, channel):
        guildid = ctx.guild.id
        cursor.execute(f'UPDATE public."prefixDB" SET channel_for_greeting = \'{channel}\' WHERE guild_id = \'{guildid}\';')
        conn.commit()

def setup(bot):
    bot.add_cog(member_greeting(bot))