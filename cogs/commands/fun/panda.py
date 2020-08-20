import discord
from discord.ext import commands
import requests
import json


class FunPanda(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def panda(self, ctx):
        request = requests.get('https://some-random-api.ml/img/panda')
        json_data = json.loads(request.text)

        embed = discord.Embed(
            title = 'Пандочка..., ня!',
            timestamp = ctx.message.created_at,
            colour = discord.Color.blue()
        )
        embed.set_image(
            url = json_data['link']
        )
        await ctx.send(embed = embed)
        
def setup(bot):
    bot.add_cog(FunPanda(bot))