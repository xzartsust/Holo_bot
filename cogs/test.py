import discord
from discord.ext import commands
import time



class Test(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.start = time.monotonic()
        self.result = time.monotonic() - self.start
    
    @commands.command()
    @commands.is_owner()
    async def test(self, ctx):
        await ctx.send("Program time: {:>.3f}".format(self.result) + " seconds.")
        
def setup(bot):
    bot.add_cog(Test(bot))