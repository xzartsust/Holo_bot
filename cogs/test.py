import discord
from discord.ext import commands
import requests
import json
from discord.utils import get
import asyncio


class Test(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        
    @commands.command()
    @commands.is_owner()
    async def test(self, ctx):
        await ctx.send()

def setup(bot):
    bot.add_cog(Test(bot))