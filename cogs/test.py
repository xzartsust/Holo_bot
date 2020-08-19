import discord
from discord.ext import commands


class Test(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        
    @commands.command()
    @commands.is_owner()
    async def test(self, ctx):
        for i in range(len(ctx.message.guild.features, i+1)):
            while i < len(ctx.message.guild.features):
                print('1')
        
def setup(bot):
    bot.add_cog(Test(bot))