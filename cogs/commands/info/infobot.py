import discord
from discord.ext import commands
import time
import datetime as DT

start = time.monotonic()

class InfoBot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def infobot(self, ctx):
        await ctx.channel.purge(limit = 1)

        result = time.monotonic() - start

        embed=discord.Embed(
            title="Инфорация про бота\n ",
            timestamp = ctx.message.created_at,
            colour = discord.Color.purple()
        )
        embed.add_field(
            name="Библиотека",
            value="discord.py",
            inline=False
        )
        embed.add_field(
            name="Состояние",
            value="Beta", 
            inline=False
        )
        embed.add_field(
            name="Версия",
            value="0.0.3 Beta",
            inline=True
        )
        embed.add_field(
            name="Сайт",
            value="Скоро...",
            inline=True
        )
        embed.add_field(
            name="Support server",
            value="https://discord.gg/8f4KUp",
            inline=False
        )
        embed.add_field(
            name='Время с последнего запуска',
            value= DT.timedelta(seconds=result)
        )
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(InfoBot(bot))
