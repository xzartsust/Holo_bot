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
    async def run_code(self, ctx, *, code: str = None):

        try:
            
            c = eval(f'{code}')
            await ctx.send(f'```{c}```')

        except Exception as e:
            print(f'[{ctx.message.created_at}] [{ctx.message.guild.name}] [{ctx.message.guild.owner}] - [{e}]')
    
    async def cog_command_error(self, ctx: commands.Context, error: commands.CommandError):
        await ctx.send('Произошла ошибка: {}'.format(str(error)))
        print(f'[{ctx.message.created_at}] [{ctx.message.guild.name}] [{ctx.message.guild.owner}] - [{error}]')
        
def setup(bot):
    bot.add_cog(comp_code(bot))

bot_owner = os.environ.get('bot_owner')
