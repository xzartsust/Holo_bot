import discord
from discord.ext import commands
import pyttsx3

class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def test(self, ctx):
        pass

def setup(bot):
    bot.add_cog(Test(bot))