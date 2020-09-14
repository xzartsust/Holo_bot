import discord
from discord.ext import commands
import requests
import json

class FunFox(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def fox(self, ctx):
        response = requests.get('https://some-random-api.ml/img/fox')
        json_data = json.loads(response.text)

        embed = discord.Embed(
            title = 'Лисичка..., няя!',
            colour = discord.Color.blue()
        )
        embed.set_image(
            url = json_data['link']
        )
        await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(FunFox(bot))