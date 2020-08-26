import discord
from discord.ext import commands
import requests
import json
from discord.utils import get
import asyncio
import aiohttp


class Test(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        
    @commands.command()
    @commands.is_owner()
    async def test(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://nekos.life') as r:
                if r.status == 200:
                    js = await r.json()
                    await ctx.send(js['file'])
def setup(bot):
    bot.add_cog(Test(bot))