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
            title = f'Приветствуем Вас на официальном сервере\nподдержки бота {self.bot.user.name}!',
            description = f'Каждый участник этого сервере равен перед другими и любимый и уважаемый, но все же гость. Поэтому настоятельно просим ознакомиться с каналом #rules\nЗаранее благодарим Вас за вежливость и адекватность.'
        )
        emb.add_field(
            name = 'У нас есть две категории **Сhats for English speakers** и **Сhats for Russian speakers**',
            value='!'
        )

        await channel.send(f'{member.mention}', embed = emb)
    
    @commands.command(aliases=['wlc'])
    async def welcome(self, ctx, channel):
        guildid = ctx.guild.id
        cursor.execute(f'UPDATE public."prefixDB" SET channel_for_greeting = \'{channel}\' WHERE guild_id = \'{guildid}\';')
        conn.commit()

def setup(bot):
    bot.add_cog(member_greeting(bot))