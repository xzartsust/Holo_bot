import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup

class FunNSFWNekoLewd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_nsfw()
    async def nekolewd(self, ctx):
        response = requests.get('https://nekos.life/lewd')
        html = response.text
        soup = BeautifulSoup(html,'html.parser')
        img = soup.find('img')['src']

        embed = discord.Embed(
            title = 'Кошечка... Как еротишненько :relaxed:',
            timestamp = ctx.message.created_at,
            colour = discord.Color.blue()
        )
        embed.set_image(
            url=img
        )
        await ctx.send(embed = embed)
    
    @nekolewd.error
    async def hololewd_error(self, ctx, error):
        if isinstance(error, commands.NSFWChannelRequired):
            emb = discord.Embed(
                timestamp= ctx.message.created_at, 
                title='Ошибка!!!', colour=discord.Color.red(), 
                description='В канале выключен режим NSFW'
                )
            emb.set_footer(text= ctx.message.author)
            await ctx.channel.purge(limit=1)
            await ctx.send(embed=emb)

def setup(bot):
    bot.add_cog(FunNSFWNekoLewd(bot))