import discord
from discord.ext import commands
import requests
import json


class FunPat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def pat(self, ctx , member = None):
        request = requests.get('https://some-random-api.ml/animu/pat')
        json_data = json.loads(request.text)

        embed = discord.Embed(
            title = member.mention + 'погладил!',
            timestamp = ctx.message.created_at,
            colour = discord.Color.blue()
        )
        embed.set_image(
            url = json_data['link']
        )
        await ctx.send(embed = embed)
        
def setup(bot):
    bot.add_cog(FunPat(bot))