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

    @commands.group(name='help',aliases=['helpcmd','i','helpcommands'], invoke_without_command=True)
    async def help_for_commands(self, ctx):
        await ctx.channel.purge(limit=1)

        emb= discord.Embed(title=f'Команды бота {self.bot.user.name}', description='Здесь вы узнаете информацию про все команды бота\n')
        emb.add_field(name='**Другая информация**',value='Чтобы получить больше информации о какой либо команде, вы можете написать: {}help `команда` \nТак же, вы можете нажать на реакцию под сообщением, чтобы переключить страницу.\n'.format(PREFIX))
        emb1= discord.Embed(title='Команды информации', description='Что бы узнать больше о команде напишите {}help [команда]. \n**Пример**: {}help user'.format(PREFIX,PREFIX))
        emb1.add_field(name='**Команды**', value=f'`{PREFIX}user` или `{PREFIX}userinfo` или `{PREFIX}ui` или `{PREFIX}infouser`\n`{PREFIX}ping`\n`{PREFIX}bot_server`\n`{PREFIX}tuser`')
        
        '''
        emb1.add_field(name='`{}user`'.format(PREFIX),value=' - Информация про пользователя', inline=False)
        emb1.add_field(name='`{}ping`'.format(PREFIX),value=' - Посмотреть пинг бота', inline=False)
        emb1.add_field(name='`{}bot_servers`'.format(PREFIX),value=' - Посмотреть на скольких серверах есть етот бот', inline=False)
        emb1.add_field(name='`{}tuser`'.format(PREFIX), value=' - Посмотреть сколько всего человек используют этого бота',inline=False)
        '''
        emb2=discord.Embed(title='Команды модерации', description='Скоро...')

        embeds=[emb,emb1,emb2]
        message= await ctx.send(embed= emb)
        page= pag(self.bot, message, only=ctx.author, use_more=False, embeds=embeds, color=0x008000, time_stamp=True)

        await page.start()
    
    @help_for_commands.command(name='user')
    async def user_subcommands(self, ctx):
        user_emb=discord.Embed(title='Информацыя про команду: .user',description='**Команда**: `[user]` или `[userinfo]` или `[infouser]` или `[iu]`\n **Описание**: показивает информацию про пользователя')
        

        await ctx.send(embed=user_emb)





def setup(bot):
    bot.add_cog(HelpCommands(bot))
