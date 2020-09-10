import discord
from discord.ext import commands


class bot_ready(commands.Cog):
    def __init__(self, bot):
        self.bot= bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Logged in as:\n{0.user.name}\n{0.user.id}\n'.format(self.bot))
    

def setup(bot):
    bot.add_cog(bot_ready(bot))
