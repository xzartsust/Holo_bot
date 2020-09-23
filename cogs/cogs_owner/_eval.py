import discord
from discord.ext import commands
import os
import discord
from discord import utils
from discord.ext.commands import Bot
from discord.utils import get
from datetime import datetime
import time
import asyncio
from itertools import cycle
from Cybernator import Paginator as pag
import psycopg2
import asyncpg, asyncio
import random

def is_owner(ctx):
    return ctx.author.id == bot_owner

class comp_code(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(aliases=['eval'])
    @commands.is_owner()
    async def run_code(self, ctx, *, code: str):

        try:
            c = eval(f'{code}')
            await ctx.send(f'```{c}```')

        except commands.NotOwner:
            await ctx.send('Эту команду имеет право использовать только создатель бота')
        except Exception as e:
            print(e)

def setup(bot):
    bot.add_cog(comp_code(bot))

bot_owner = os.environ.get('bot_owner')
