import discord
from discord.ext import commands
from Cybernator import Paginator as pag


class invite(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def invite(self, ctx):
        
        emb = discord.Embed(
            timestamp = ctx.message.created_at,
            title = f'Мои силки',
            description = 'Так же, вы можете нажать на реакцию под сообщением, чтобы получить больше силок',
        )
        emb1 = discord.Embed(
            title='Мой инвайт',
            url='https://discord.com/api/oauth2/authorize?client_id=729957701240750140&permissions=2147483639&scope=bot'
        )
        embeds = [emb,emb1]
        message = await ctx.send(embed= emb)
        page = pag(self.bot, message, only=ctx.author, use_more=False, embeds=embeds, color=0xFFFF00, time_stamp=True)
    
        await page.start()
        


def setup(bot):
    bot.add_cog(invite(bot))