import discord
from discord.ext import commands
from datetime import datetime
import os
import time
from Cybernator import Paginator as pag
import asyncpg, asyncio
import psycopg2


database = os.environ.get('DATABASE')
user = os.environ.get('USER')
password = os.environ.get('PASSWORD')
host = os.environ.get('HOST')
port = os.environ.get('PORT')

conn = psycopg2.connect(
    database = f"{database}", 
    user = f"{user}", 
    password = f"{password}", 
    host = f"{host}", 
    port = "5432"
)
cursor = conn.cursor()

def prefix_in_guild(bot,message):
    guildid = message.guild.id
    cursor.execute(f'SELECT prefix FROM public."prefixDB" WHERE guild_id = \'{guildid}\';')
    prefix = cursor.fetchone()
    conn.commit()
    
    return prefix


class HelpCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(name='help',aliases=['helpcmd','i','helpcommands'], invoke_without_command=True)
    async def help_for_commands(self, ctx):
        await ctx.channel.purge(limit=1)

        emb= discord.Embed(title=f'Команды бота {self.bot.user.name}', description='Здесь вы узнаете информацию про все команды бота\n')
        emb.add_field(name='**Другая информация**',value='Чтобы получить больше информации о какой либо команде, вы можете написать: {}help `команда` \nТак же, вы можете нажать на реакцию под сообщением, чтобы переключить страницу.\n'.format(prefix_in_guild))
        
        emb1= discord.Embed(title='Команды информации', description='Что бы узнать больше о команде напишите {}help [команда]. \n**Пример**: {}help user'.format(prefix_in_guild,prefix_in_guild))
        emb1.add_field(name='**Команды**', value=f'`{prefix_in_guild}user`\n`{prefix_in_guild}ping`\n`{prefix_in_guild}bot_servers`\n`{prefix_in_guild}tuser`\n')
        
        emb2=discord.Embed(title='Команды администрации', description=f'`{prefix_in_guild}change_prefix` или `{prefix_in_guild}prefix`')

        embeds=[emb,emb1,emb2]
        message= await ctx.send(embed= emb)
        page= pag(self.bot, message, only=ctx.author, use_more=False, embeds=embeds, color=0x008000, time_stamp=True)

        await page.start()
    
    @help_for_commands.command(name='user')
    async def user_subcommands(self, ctx):
        user_emb=discord.Embed(title=f'Информация про команду: {prefix_in_guild}user', colour = discord.Color.teal(), description=f'**Команда**: `[user]` или `[userinfo]` или `[infouser]` или `[iu]` или `[ui]`\n**Описание**: показивает информацию про пользователя\n**Использования**: `{prefix_in_guild}user` или `{prefix_in_guild}userinfo` или `{prefix_in_guild}infouser` или `{prefix_in_guild}iu` или `{prefix_in_guild}ui`, или если вы хотите узнать информацию о другом пользователя, то после команды пропишите тег пользователя о котором хотите узнать информацию\n**Пример**: `{prefix_in_guild}user @имя_пользователя`')
        await ctx.send(embed=user_emb)

    @help_for_commands.command(name='ping')
    async def pind_subcommands(self,ctx):
        ping_emb=discord.Embed(title=f'Информация про команду: {prefix_in_guild}ping',colour = discord.Color.teal(), description=f'**Команда**: `[ping]`\n**Описание**: показивает пинг бота\n**Использования**: `{prefix_in_guild}ping`')
        await ctx.send(embed=ping_emb)

    @help_for_commands.command(name='bot_servers')
    async def botservers_subcommands(self,ctx):
        botservers_emb=discord.Embed(title=f'Информация про команду: {prefix_in_guild}bot_servers',colour = discord.Color.teal(), description=f'**Команда**: `[bot_servers]`\n**Описание**: показивает на сколько серверах присутствует этот бот\n**Использования**: `{prefix_in_guild}bot_servers`')
        await ctx.send(embed=botservers_emb)   

    @help_for_commands.command(name='tuser')
    async def tuser_subcommands(self,ctx):
        tuser_emb=discord.Embed(title=f'Информация про команду: {prefix_in_guild}tuser',colour = discord.Color.teal(), description=f'**Команда**: `[tuser]`\n**Описание**: показивает сколько людей используют этого бота\n**Использования**: `{prefix_in_guild}tuser`')
        await ctx.send(embed=tuser_emb)   





def setup(bot):
    bot.add_cog(HelpCommands(bot))
