import discord
from discord.ext import commands
import time
start = time.time()
finish = time.time()
result = finish - start
print("Program time: " + str(result) + " seconds.")


class Test(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def test(self, ctx):
        await ctx.send(str(result))
        
def setup(bot):
    bot.add_cog(Test(bot))