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
        role = self.bot.get_role(745261928208924762)
        await ctx.send(role)

def setup(bot):
    bot.add_cog(Test(bot))