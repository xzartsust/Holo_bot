import discord
from discord.ext import commands
import requests


class Test(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        
    @commands.command()
    @commands.is_owner()
    async def test(self, ctx):
        request = requests.get('https://some-random-api.ml/img/fox')
        embed = discord.Embed(
            title = 'Fox'
        )
        embed.set_image(
            url= request['link']
        )        
        await ctx.send(embed = embed)
def setup(bot):
    bot.add_cog(Test(bot))