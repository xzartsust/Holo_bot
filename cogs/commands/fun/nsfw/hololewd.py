import discord
from discord.ext import commands
import requests
import json

class FunHoloLewd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_nsfw()
    async def hololewd(self, ctx):
        response = requests.get('https://nekos.life/api/v2/img/hololewd')
        json_data = json.loads(response.text)
        img = json_data['url']

        embed = discord.Embed(
            title = 'Холочка... Как еротишненько :relaxed:',
            timestamp = ctx.message.created_at,
            colour = discord.Color.blue()
        )
        embed.set_image(
            url=img
        )
        await ctx.send(embed = embed)
    
    @hololewd.error
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
    bot.add_cog(FunHoloLewd(bot))