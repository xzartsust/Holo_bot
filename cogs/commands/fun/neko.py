import discord
from discord.ext import commands
from bs4 import BeautifulSoup
import requests


class FunNeko(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def neko(self, ctx):
        response = requests.get('https://nekos.life/')
        html = response.text
        soup = BeautifulSoup(html,'html.parser')
        img = soup.find('img')['src']

        embed = discord.Embed(
            title = 'Кошечка... :relaxed:',
            timestamp = ctx.message.created_at
        )
        embed.set_image(
            url=img
        )
        await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(FunNeko(bot))