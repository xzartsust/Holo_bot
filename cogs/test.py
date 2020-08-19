import discord
from discord.ext import commands


class Test(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        
    @commands.command()
    @commands.is_owner()
    async def test(self, ctx):
        i = len(ctx.message.guild.features)
        for i in range(0, i+1):
            while i < len(ctx.message.guild.features):
                print('1')
        
def setup(bot):
    bot.add_cog(Test(bot))