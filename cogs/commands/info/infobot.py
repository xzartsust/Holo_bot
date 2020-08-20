import discord
from discord.ext import commands
import time
import datetime as DT
import os

start = time.monotonic()

class InfoBot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def infobot(self, ctx):
        await ctx.channel.purge(limit = 1)
        
        owner_bot = self.bot.get_user(bot_owner)
        result = time.monotonic() - start

        embed=discord.Embed(
            title=":information_source:BOT INFORMATION:information_source:",
            timestamp = ctx.message.created_at,
            colour = discord.Color.purple()
        )
        embed.add_field(
            name = 'Developer',
            value = f'```{owner_bot}```'
        )
        embed.add_field(
            name="Библиотека",
            value="```discord.py```",
            inline=False
        )
        embed.add_field(
            name="Состояние",
            value="```Beta```", 
            inline=False
        )
        embed.add_field(
            name="Версия",
            value="```0.0.3 Beta```",
            inline=True
        )
        embed.add_field(
            name="Сайт",
            value="```Скоро...```",
            inline=True
        )
        embed.add_field(
            name="Support server",
            value="https://discord.gg/8f4KUp",
            inline=False
        )
        embed.add_field(
            name='Время с последнего запуска',
            value= f'```{DT.timedelta(seconds=result)}```'
        )
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(InfoBot(bot))

bot_owner = os.environ.get('bot_owner')