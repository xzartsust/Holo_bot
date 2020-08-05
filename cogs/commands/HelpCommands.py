import discord
from discord import utils
from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import get
from datetime import datetime
import logging
import time
from Cybernator import Paginator as pag

PREFIX = '.'


class HelpCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(aliases=['helpcmd','i','help','helpcommands'])
    async def help_for_commands(self, ctx):
        await ctx.channel.purge(limit=1)

        emb= discord.Embed(title='Помощ по использованию бота', description='Здесь вы можете узнать про осноные команды бота')

        emb1= discord.Embed(title='Команды бота')
        emb1.add_field(name='`{}help` или `{}info` или `{}i`'.format(PREFIX, PREFIX, PREFIX), value=' - Команды бота',inline=False)
        emb1.add_field(name='`{}prefix`'.format(PREFIX), value=' - Изменить префикс бота',inline=False)
        emb1.add_field(name='`{}user @имя`'.format(PREFIX),value=' - Информация про пользователя', inline=False)
        emb1.add_field(name='`{}ping`'.format(PREFIX),value=' - Посмотреть пинг бота', inline=False)
        emb1.add_field(name='`{}bot_servers`'.format(PREFIX),value=' - Посмотреть на скольких серверах есть етот бот', inline=False)
        emb1.add_field(name='`{}tuser`'.format(PREFIX), value=' - Посмотреть сколько всего человек используют этого бота',inline=False)

        emb2=discord.Embed(title='Команды для модерации', description='Скоро...')

        embeds=[emb,emb1,emb2]
        message= await ctx.send(embed= emb)
        page= pag(self.bot, message, only=ctx.author, use_more=False, embeds=embeds, color=0x008000, delete_message=True,time_stamp=True)

        await page.start()


def setup(bot):
    bot.add_cog(HelpCommands(bot))
