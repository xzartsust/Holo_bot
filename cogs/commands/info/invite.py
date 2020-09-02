import discord
from discord.ext import commands
from Cybernator import Paginator as pag


class invite(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def invite(self, ctx):
        await ctx.channel.purge(limit = 1)
        
        emb = discord.Embed(
            timestamp = ctx.message.created_at,
            title = f'Мои силки | My links',
            description = 'Пролистайте страницу чтобы получить силки | Scroll the page to get links',
        )
        emb1 = discord.Embed(
            title='Пригласи меня | Invite me',
            url='https://discord.com/api/oauth2/authorize?client_id=729957701240750140&permissions=2081422583&scope=bot'
        )
        emb2 = discord.Embed(
            title='Мой сервер поддержки | My support server',
            url = 'https://discord.gg/4FpZepm'
        )
        embeds = [emb,emb1,emb2]
        message = await ctx.send(embed= emb)
        page = pag(self.bot, message, only=ctx.author, use_more=False, embeds=embeds, color=0xFFFF00, time_stamp=True)
    
        await page.start()
        


def setup(bot):
    bot.add_cog(invite(bot))