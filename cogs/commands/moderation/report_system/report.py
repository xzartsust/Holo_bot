import discord
from discord.ext import commands
from discord.utils import get

class ReportUser(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 21600, commands.BucketType.member)
    async def report(self, ctx, member: discord.Member = None, reason: str = None):
        
        guild = ctx.message.guild
        if member and reason is None:
            async for user in guild.members:
                print(user)

def setup(bot):
    bot.add_cog(ReportUser(bot))