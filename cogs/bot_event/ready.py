import discord
from discord.ext import commands


class bot_ready(commands.Cog):
    def __init__(self, bot):
        self.bot= bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Connect is {self.bot.user.name}\n')
    

def setup(bot):
    bot.add_cog(bot_ready(bot))
