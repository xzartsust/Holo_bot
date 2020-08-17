import discord
from discord.ext import commands

class Test(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command
    @commands.is_owner
    async def test(self, bot):
        channel = 743808275077922927
        await bot.send_message(channel, 'ok')
        
def setup(bot):
    bot.add_cog(Test(bot))