import discord
from discord.ext import commands
from discord.utils import get

class ReportUser(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 21600, commands.BucketType.member)
    async def report(self, ctx, member: discord.Member, reason: str = None):
        
        guild = ctx.message.guild

        for user in guild.members:
            if user.guild_permissions.administrator is True:
                us = self.bot.get_user(user.id)
                await us.send('1')

def setup(bot):
    bot.add_cog(ReportUser(bot))