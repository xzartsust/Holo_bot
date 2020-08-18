import discord
from discord.ext import commands
import time

start = time.monotonic()



class Test(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        
    @commands.command()
    @commands.is_owner()
    async def test(self, ctx):
        result = time.monotonic() - start
        await ctx.send("Program time: {:>.3f}".format(result) + " seconds.")
        
def setup(bot):
    bot.add_cog(Test(bot))