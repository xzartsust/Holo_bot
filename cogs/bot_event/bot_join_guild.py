import discord
from discord.ext import commands

class bot_join_guild(commands.Cog):
    def __init__(self, bot):
        self.bot = bot




def setup(bot):
    bot.add_cog(bot_join_guild(bot))