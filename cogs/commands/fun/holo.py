import discord
from discord.ext import commands
import requests
import json

class FunHolo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def holo(self, ctx):
        response = requests.get('https://nekos.life/api/v2/img/holo')
        json_data = json.loads(response.text)
        img = json_data['url']

        embed = discord.Embed(
            title = 'Холочка... :relaxed:',
            timestamp = ctx.message.created_at,
            colour = discord.Color.blue()
        )
        embed.set_image(
            url=img
        )
        await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(FunHolo(bot))
