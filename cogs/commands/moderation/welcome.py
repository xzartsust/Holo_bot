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
        
        cursor.execute(f'SELECT true_or_false FROM public."prefixDB" WHERE guild_id = \'{join_guild_id}\';')
        yes_or_not = cursor.fetchone()
        conn.commit()
        
        channel = self.bot.get_channel(chan[0])
        print(yes_or_not[0]) 
        
        emb = discord.Embed(
            title = f'Приветствуем Вас на сервере {member.guild.name}!',
            description = f'Каждый участник этого сервере равен перед другими. Поэтому настоятельно просим ознакомиться с правилами сервера\nЗаранее благодарим Вас за вежливость и адекватность.',
            colour = discord.Color.green()
        )
        emb.set_thumbnail(
            url = member.avatar_url
        )
        emb.set_footer(
            text = f'{member.id}' + ' Приятного времяпрепровождения!',
            icon_url= 'https://github.com/xzartsust/holo_bot/blob/master/files/image/id.png?raw=true'
        )
        
        await channel.send(f'{member.mention}', embed = emb)
    
    @commands.command(aliases=['wlc'])
    async def welcome(self, ctx, channel):
        guildid = ctx.guild.id
        cursor.execute(f'UPDATE public."prefixDB" SET channel_for_greeting = \'{channel}\' WHERE guild_id = \'{guildid}\';')
        conn.commit()

def setup(bot):
    bot.add_cog(member_greeting(bot))