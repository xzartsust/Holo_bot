import discord
from discord.ext import commands

class Test(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def test(self, ctx):
        e = discord.Embed(title='foo')
        await ctx.send('Hello', embed=e)
        
def setup(bot):
    bot.add_cog(Test(bot))