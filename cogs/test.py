import discord
from discord.ext import commands
import requests
import json
from discord.utils import get


class Test(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        
    @commands.command()
    @commands.is_owner()
    async def test(self, ctx):
        async for guild in client.fetch_guilds(limit=150):
            print(guild.name)

def setup(bot):
    bot.add_cog(Test(bot))