import discord
from discord.ext import commands
import requests
import json


class FunAnimeErotic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_nsfw()
    async def aniero(self, ctx):
        try:
         
            request = requests.get('https://nekos.life/api/v2/img/erofeet')
            json_data = json.loads(request.text)

            embed = discord.Embed(
                title = 'Как еротишненько :relaxed:',
                timestamp = ctx.message.created_at,
                colour = discord.Color.blue()
            )
            embed.set_image(
                url = json_data['url']
            )
            await ctx.send(embed = embed)
        
        except Exception as e:
            print(e)

    @aniero.error
    async def aniero_error(self, ctx, error):
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
    bot.add_cog(FunAnimeErotic(bot))