import discord
from discord.ext import commands
import requests
import json


class FunPoke(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def poke(self, ctx):
        request = requests.get('https://nekos.life/api/v2/img/poke')
        json_data = json.loads(request.text)

        embed = discord.Embed(
            title = '',
            timestamp = ctx.message.created_at,
            colour = discord.Color.blue()
        )
        embed.set_image(
            url = json_data['url']
        )
        await ctx.send(f'{ctx.message.author.mention}' + ' тыкнул!' ,embed = embed)
        
def setup(bot):
    bot.add_cog(FunPoke(bot))