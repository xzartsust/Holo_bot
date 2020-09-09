import discord
from discord.ext import commands


class CountMember(commands.Cog):
    def __init__(self , bot):
        self.bot = bot
    
    


def setup(bot):
    bot.add_cog(CountMember(bot))