import discord
from discord.ext import commands
import requests
import json


class FunTickle(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def tickle(self, ctx):
        request = requests.get('https://nekos.life/api/v2/img/tickle')
        json_data = json.loads(request.text)

        embed = discord.Embed(
            title = 'Защекочу, защекочу!',
            timestamp = ctx.message.created_at,
            colour = discord.Color.blue()
        )
        embed.set_image(
            url = json_data['link']
        )
        await ctx.send(embed = embed)
        
def setup(bot):
    bot.add_cog(FunTickle(bot))