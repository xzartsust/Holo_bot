import discord
from discord.ext import commands

class InfoBot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def infobot(self, ctx):
        await ctx.channel.purge(limit = 1)
        embed=discord.Embed(title="Инфорация про бота\n ")
        embed.add_field(name="Библиотека", value="discord.py", inline=False)
        embed.add_field(name="Состояние", value="Beta", inline=False)
        embed.add_field(name="Версия", value="0.0.3 Beta", inline=True)
        embed.add_field(name="Сайт", value="Скоро...", inline=True)
        embed.add_field(name="Support server", value="https://discord.gg/8f4KUp", inline=False)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(InfoBot(bot))
