######################################################## libraries #########################################################


import discord
from discord import utils
from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import get
import os
from datetime import datetime
import logging
import time
import asyncio
from itertools import cycle
from Cybernator import Paginator as pag
import psycopg2
import asyncpg, asyncio


########################################################## Connect to SQL ###################################################


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


########################################################################################################################


def get_prefix(bot, message):
    guildid = message.guild.id
    cursor.execute(f'SELECT prefix FROM public."prefixDB" WHERE guild_id = \'{guildid}\';')
    prefix = cursor.fetchone()
    conn.commit()
    
    return prefix

bot =commands.Bot(command_prefix = get_prefix, help_command=None)


############################################################# Events bot #################################################


async def change_status():
    await bot.wait_until_ready()
    msg= cycle(status)

    while not bot.is_closed():
        next_status= next(msg)
        await bot.change_presence(activity= discord.Game(name=next_status))
        await asyncio.sleep(13)
status=['Модернизирует свой код','t!help']


################################################## Cogs commands #################################################################


bot.load_extension('cogs.commands.info.user')
bot.load_extension('cogs.commands.info.help_commands')
bot.load_extension('cogs.commands.moderation.news')
bot.load_extension('cogs.commands.moderation.prefix')
bot.load_extension('cogs.commands.moderation.clear')
bot.load_extension('cogs.commands.info.ping')
bot.load_extension('cogs.commands.info.invite')
bot.load_extension('cogs.commands.moderation.welcome')
bot.load_extension('cogs.test')
bot.load_extension('cogs.commands.info.botservers')
bot.load_extension('cogs.commands.info.tuser')
bot.load_extension('cogs.commands.info.infobot')


################################################## Cogs owner commands #################################################################


bot.load_extension('cogs.cogs_owner.out')
bot.load_extension('cogs.cogs_owner._eval')


################################################# Cogs Event ######################################################################


bot.load_extension('cogs.bot_event.ready')
bot.load_extension('cogs.bot_event.on_guild_join')
bot.load_extension('cogs.bot_event.on_guild_remove')


TOKEN = os.environ.get('TOKEN')

bot.loop.create_task(change_status())
bot.run(TOKEN)
