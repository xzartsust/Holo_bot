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

def get_prefix(bot, message):
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
        emb.add_field(name='**Другая информация**',value=f'Чтобы получить больше информации о какой либо команде, вы можете написать: {get_prefix(ctx.message)}help `команда` \nТак же, вы можете нажать на реакцию под сообщением, чтобы переключить страницу.\n')
        
        emb1= discord.Embed(title='Команды информации', description=f'Что бы узнать больше о команде напишите {get_prefix}help [команда]. \n**Пример**: {get_prefix}help user')
        emb1.add_field(name='**Команды**', value=f'`{get_prefix}user`\n`{get_prefix}ping`\n`{get_prefix}bot_servers`\n`{get_prefix}tuser`\n')
        
        emb2=discord.Embed(title='Команды администрации', description=f'`{get_prefix}change_prefix` или `{get_prefix}prefix`')

        embeds=[emb,emb1,emb2]
        message= await ctx.send(embed= emb)
        page= pag(self.bot, message, only=ctx.author, use_more=False, embeds=embeds, color=0x008000, time_stamp=True)
    
        await page.start()
    
    @help_for_commands.command(name='user', aliases=['userinfo','ui','infouser','iu'])
    async def user_subcommands(self, ctx):
        user_emb=discord.Embed(title=f'Информация про команду: {get_prefix}user', colour = discord.Color.teal(), description=f'**Команда**: `[user]` или `[userinfo]` или `[infouser]` или `[iu]` или `[ui]`\n**Описание**: показивает информацию про пользователя\n**Использования**: `{get_prefix}user` или `{get_prefix}userinfo` или `{get_prefix}infouser` или `{get_prefix}iu` или `{get_prefix}ui`, или если вы хотите узнать информацию о другом пользователя, то после команды пропишите тег пользователя о котором хотите узнать информацию\n**Пример**: `{get_prefix}user @имя_пользователя`')
        await ctx.send(embed=user_emb)

    @help_for_commands.command(name='ping')
    async def pind_subcommands(self,ctx):
        ping_emb=discord.Embed(title=f'Информация про команду: {get_prefix}ping',colour = discord.Color.teal(), description=f'**Команда**: `[ping]`\n**Описание**: показивает пинг бота\n**Использования**: `{get_prefix}ping`')
        await ctx.send(embed=ping_emb)

    @help_for_commands.command(name='bot_servers')
    async def botservers_subcommands(self,ctx):
        botservers_emb=discord.Embed(title=f'Информация про команду: {get_prefix}bot_servers', colour = discord.Color.teal(), description=f'**Команда**: `[bot_servers]`\n**Описание**: показивает на сколько серверах присутствует этот бот\n**Использования**: `{get_prefix}bot_servers`')
        await ctx.send(embed=botservers_emb)   

    @help_for_commands.command(name='tuser')
    async def tuser_subcommands(self,ctx):
        tuser_emb=discord.Embed(title=f'Информация про команду: {get_prefix}tuser', colour = discord.Color.teal(), description=f'**Команда**: `[tuser]`\n**Описание**: показивает сколько людей используют этого бота\n**Использования**: `{get_prefix}tuser`')
        await ctx.send(embed=tuser_emb)   

def setup(bot):
    bot.add_cog(HelpCommands(bot))
