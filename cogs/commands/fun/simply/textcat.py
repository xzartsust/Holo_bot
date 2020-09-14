import discord
from discord.ext import commands
import nekos

class FunTextCat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def tcat(self, ctx):
        await ctx.send(nekos.textcat())

def setup(bot):
    bot.add_cog(FunTextCat(bot))