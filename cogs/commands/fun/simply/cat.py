import discord
from discord.ext import commands
import requests
import json


class FunCat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def cat(self, ctx):
        request = requests.get('https://nekos.life/api/v2/img/meow')
        json_data = json.loads(request.text)

        embed = discord.Embed(
            title = 'Котик..., ня!',
            timestamp = ctx.message.created_at,
            colour = discord.Color.blue()
        )
        embed.set_image(
            url = json_data['link']
        )
        await ctx.send(embed = embed)
        
def setup(bot):
    bot.add_cog(FunCat(bot))