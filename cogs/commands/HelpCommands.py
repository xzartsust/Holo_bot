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
        emb1.add_field(name='**Команды**', value=f'`{PREFIX}user`\n`{PREFIX}ping`\n`{PREFIX}bot_servers`\n`{PREFIX}tuser`')
        
        emb2=discord.Embed(title='Команды модерации', description='Скоро...')

        embeds=[emb,emb1,emb2]
        message= await ctx.send(embed= emb)
        page= pag(self.bot, message, only=ctx.author, use_more=False, embeds=embeds, color=0x008000, time_stamp=True)

        await page.start()
    
    @help_for_commands.command(name='user',aliases=['infouser','ui','userinfo','iu'])
    async def user_subcommands(self, ctx):
        user_emb=discord.Embed(title=f'Информация про команду: {PREFIX}user',description=f'**Команда**: `[user]` или `[userinfo]` или `[infouser]` или `[iu]` или `[ui]`\n**Описание**: показивает информацию про пользователя\n**Использования**: `{PREFIX}user` или `{PREFIX}userinfo` или `{PREFIX}infouser` или `{PREFIX}iu` или `{PREFIX}ui`, или если вы хотите узнать информацию о другом пользователя, то после команды пропишите тег пользователя о котором хотите узнать информацию\n**Пример**: `{PREFIX}user @имя_пользователя`')
        await ctx.send(embed=user_emb)

    @help_for_commands.command(name='ping')
    async def pind_subcommands(self,ctx):
        ping_emb=discord.Embed(title=f'Информация про команду: {PREFIX}ping', description=f'**Команда**: `[ping]`\n**Описание**: показивает пинг бота\n**Использования**: `{PREFIX}ping`')
        await ctx.send(embed=ping_emb)

    @help_for_commands.command(name='bot_servers')
    async def botservers_subcommands(self,ctx):
        botservers_emb=discord.Embed(title=f'Информация про команду: {PREFIX}bot_servers', description=f'**Команда**: `[bot_servers]`\n**Описание**: показивает на сколько серверах присутствует этот бот\n**Использования**: `{PREFIX}bot_servers`')
        await ctx.send(embed=botservers_emb)   

    @help_for_commands.command(name='tuser')
    async def tuser_subcommands(self,ctx):
        tuser_emb=discord.Embed(title=f'Информация про команду: {PREFIX}tuser', description=f'**Команда**: `[tuser]`\n**Описание**: показивает сколько людей используют этого бота\n**Использования**: `{PREFIX}tuser`')
        await ctx.send(embed=tuser_emb)   





def setup(bot):
    bot.add_cog(HelpCommands(bot))
