import discord
from discord.ext import commands


class invite(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def invite(self, ctx):
        
        emb = discord.Embed(
            timestamp = ctx.message.created_at,
            title = 'Мои силки',
            description = '',
        )
        emb.set_thumbnail(url='https://discord.com/api/oauth2/authorize?client_id=729957701240750140&permissions=2147483639&scope=bot')
        
        await ctx.send(embed= emb)


def setup(bot):
    bot.add_cog(invite(bot))