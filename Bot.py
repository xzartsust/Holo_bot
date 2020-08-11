######################################################## Библиотеки #########################################################

import discord
from discord import utils
from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import get
from config_for_bot import *
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

def get_prefix(bot,guild):
    guildid = guild.id
    prefix = cursor.execute(f'SELECT prefix FROM public."prefixDB" WHERE guild_id = \'{guildid}\';')
    conn.commit()

    print(prefix)
    return prefix

bot=commands.Bot(command_prefix=get_prefix, help_command=None)


############################################################# Events bot #################################################


async def is_owner(ctx):
    return ctx.author.id == bot_owner

async def change_status():
    await bot.wait_until_ready()
    msg= cycle(status)

    while not bot.is_closed():
        next_status= next(msg)
        await bot.change_presence(activity= discord.Game(name=next_status))
        await asyncio.sleep(13)

@bot.event
async def on_ready():
    print(f'Connect is {bot.user.name}')


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
async def ping(ctx):
    time_1 = time.perf_counter()
    await ctx.trigger_typing()
    time_2 = time.perf_counter()
    ping = round((time_2 - time_1) * 1000)
    emb= discord.Embed(description=f':ping_pong:Pong: {ping}ms',colour=discord.Color.blurple())
    await ctx.channel.purge(limit=1)
    await ctx.send(embed= emb)

@bot.command()
async def clear(ctx, arg: int):
    await ctx.channel.purge(limit= arg + 1)

@bot.command()
async def tuser(ctx):
    all_users = set([])
    for user in bot.get_all_members():
        all_users.add(user)
    await ctx.channel.purge(limit=1)
    await ctx.send('Total users in all my servers combined: ' + str(len(all_users)))


####################################################### Eval ################################################


@bot.command(aliases=['eval'])
@commands.is_owner()
async def run_code(ctx,*,code):
    await ctx.send(eval(code))


####################################################### Errors ###############################################
 

@clear.error
async def clear_error(ctx,error):
    if isinstance(error, commands.MissingPermissions):
        emb = discord.Embed(title='Ошибка!!!', colour=discord.Color.red(), description='У вас нет прав на ету команду')
        await ctx.channel.purge(limit=1)
        await ctx.send(embed=emb)

@run_code.error
async def _eval_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        emb = discord.Embed(title='Ошибка!!!', colour=discord.Color.red(), description='Эту команду имеет право использовать только создатель бота')
        await ctx.channel.purge(limit=1)
        await ctx.send(embed=emb)


################################################## Cogs commands #################################################################


bot.load_extension('cogs.commands.user')
bot.load_extension('cogs.commands.HelpCommands')
bot.load_extension('cogs.commands.news')
bot.load_extension('cogs.commands.prefix')

################################################# Cogs Event ######################################################################


#bot.load_extension('cogs.BotEvent')


TOKEN = os.environ.get('TOKEN')
bot_owner = os.environ.get('bot_owner')


bot.loop.create_task(change_status())
bot.run(TOKEN)
