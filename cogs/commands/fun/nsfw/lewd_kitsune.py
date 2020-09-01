import discord
from discord.ext import commands
import requests
import json


class FunKitsuneLewd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_nsfw()
    async def kitsunelewd(self, ctx):
        request = requests.get('https://nekos.life/api/v2/img/lewdk')
        json_data = json.loads(request.text)

        embed = discord.Embed(
            title = 'Лисичка... Как еротишненько :relaxed:',
            timestamp = ctx.message.created_at,
            colour = discord.Color.blue()
        )
        embed.set_image(
            url = json_data['link']
        )
        await ctx.send(embed = embed)
    
    @kitsunelewd.error
    async def kitsunelewd_error(self, ctx, error):
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
    bot.add_cog(FunKitsuneLewd(bot))