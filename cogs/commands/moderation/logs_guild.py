import discord
from discord.ext import commands


class GuildLogs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async for entry in guild.audit_logs(action = discord.AuditLogAction.channel_update):
        print('1')

def setup(bot):
    bot.add_cog(GuildLogs(bot))