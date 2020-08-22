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
        c = eval(code)
        await ctx.send(f'```{c}```')
'''
    @run_code.error
    async def _eval_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            emb = discord.Embed(timestamp= ctx.message.created_at, title='Ошибка!!!', colour=discord.Color.red(), description='Эту команду имеет право использовать только создатель бота')
            emb.set_footer(text=ctx.message.author)
            await ctx.channel.purge(limit=1)
            await ctx.send(embed=emb)
'''
def setup(bot):
    bot.add_cog(comp_code(bot))

bot_owner = os.environ.get('bot_owner')
