import discord
from discord.ext import commands

class ReportUser(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command
    @commands.cooldown(1, 21600, commands.BucketType.member)
    async def report(self, ctx, member: discord.Member, reason: str = None):
        
        pass

def setup(bot):
    bot.add_cog(ReportUser(bot))