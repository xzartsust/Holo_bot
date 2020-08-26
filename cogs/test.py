import discord
from discord.ext import commands
import requests
import json
from discord.utils import get
import asyncio
import aiohttp
import io


class Test(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        
    @commands.command()
    @commands.is_owner()
    async def test(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://nekos.life') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'cool_image.png'))
def setup(bot):
    bot.add_cog(Test(bot))