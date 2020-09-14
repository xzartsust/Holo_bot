import discord
from discord.ext import commands
import requests
import json


class FunNekoGif(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def nekogif(self, ctx):
        request = requests.get('https://nekos.life/api/v2/img/ngif')
        json_data = json.loads(request.text)

        embed = discord.Embed(
            title = 'Кошечка... ня! :relaxed:',
            timestamp = ctx.message.created_at,
            colour = discord.Color.blue()
        )
        embed.set_image(
            url = json_data['url']
        )
        await ctx.send(embed = embed)
        
def setup(bot):
    bot.add_cog(FunNekoGif(bot))