import discord
from discord.ext import commands
import requests
import json


class FunMemes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def memes(self, ctx):
        response = requests.get('https://some-random-api.ml/meme')
        json_data = json.loads(response.text)

        embed = discord.Embed(
            title = 'Memes',
            colour = discord.Color.blue()
        )
        embed.set_footer(
            text = json_data['caption']
        )
        embed.set_image(
            url = json_data['image']
        )
        await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(FunMemes(bot))