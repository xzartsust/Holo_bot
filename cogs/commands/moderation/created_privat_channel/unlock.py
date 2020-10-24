import discord 
from discord.ext import commands

class UnlockPrivatChannel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def unlock(self, ctx, member):
        pass

def setup(bot):
    bot.add_cog(UnlockPrivatChannel(bot))