import discord
from discord.ext import commands


class bot_ready(commands.Cog):
    def __init__(self, bot):
        self.bot= bot

    @commands.Cog.listener()
    async def on_ready(self):

        print(f'Logged in as:\n{self.bot.user.name}\n{self.bot.user.id}\n')

def setup(bot):
    bot.add_cog(bot_ready(bot))
