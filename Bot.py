######################################################## Библиотеки #########################################################

import discord
from discord import utils
from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import get
import youtube_dl
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

bot=commands.Bot(command_prefix = get_prefix, help_command=None)


############################################################# Events bot #################################################

async def change_status():
    await bot.wait_until_ready()
    msg= cycle(status)

    while not bot.is_closed():
        next_status= next(msg)
        await bot.change_presence(activity= discord.Game(name=next_status))
        await asyncio.sleep(13)
status=['Модернизирует свой код','.help']
######################################################### Commands bot ###################################################


@bot.command()
@commands.is_owner()
async def logout(ctx):
    await bot.logout()

@bot.command()
async def bot_servers(ctx):
    emb=discord.Embed(description=f'Присутствует на {str(len(bot.guilds))} серверах', colour=discord.Color.blurple())
    await ctx.send(embed= emb)


@bot.command()
async def tuser(ctx):
    all_users = set([])
    for user in bot.get_all_members():
        all_users.add(user)
    await ctx.channel.purge(limit=1)
    await ctx.send('Total users in all my servers combined: ' + str(len(all_users)))


###################################################### Errors ###############################################
 



################################################## Cogs commands #################################################################


bot.load_extension('cogs.commands.user')
bot.load_extension('cogs.commands.HelpCommands')
bot.load_extension('cogs.commands.news')
bot.load_extension('cogs.commands.prefix')
bot.load_extension('cogs.commands.clear')
bot.load_extension('cogs.commands.ping')
#bot.load_extension('')

################################################# Cogs Event ######################################################################


bot.load_extension('cogs.bot_event.ready')
bot.load_extension('cogs.bot_event.bot_join_guild')



TOKEN = os.environ.get('TOKEN')

bot.loop.create_task(change_status())
bot.run(TOKEN)
