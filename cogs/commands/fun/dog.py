import discord
from discord.ext import commands
import requests
import json


class FunDog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def dog(self, ctx):
        request = requests.get('https://random.dog/woof.json')
        json_data = json.loads(request.text)

        embed = discord.Embed(
            title = 'Собачка..., ня!',
            timestamp = ctx.message.created_at,
            colour = discord.Color.blue()
        )
        embed.set_image(
            url = json_data['link']
        )
        await ctx.send(embed = embed)
        
def setup(bot):
    bot.add_cog(FunDog(bot))