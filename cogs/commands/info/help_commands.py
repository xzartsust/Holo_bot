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

def prefix_in_guild(bot, message):
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
        global prefix 
        await ctx.channel.purge(limit=1)

        prefix_1 = prefix_in_guild(self.bot, ctx.message)
        prefix = prefix_1[0]
        
        emb= discord.Embed(
            title=f'Команды бота {self.bot.user.name}', 
            description=f'Здесь вы узнаете информацию про все команды бота\nНапишите `{prefix}invite` чтобы получить ссылки бота'
        )
        emb.add_field(
            name='**Другая информация**',
            value=f'Чтобы получить больше информации о какой либо команде, вы можете написать: `{prefix}help *команда*` \nТак же, вы можете нажать на реакцию под сообщением, чтобы переключить страницу.\n'
        )
        emb1= discord.Embed(
            title='Команды информации', 
            description=f'Что бы узнать больше о команде напишите {prefix}help [команда]. \n**Пример**: `{prefix}help user`'
        )
        emb1.add_field(
            name='**Команды**', 
            value=f'`{prefix}user`\n`{prefix}ping`\n`{prefix}botservers`\n`{prefix}tuser`\n`{prefix}infobot`\n`{prefix}serverinfo` или `{prefix}si` или `{prefix}is`'
        )
        emb2=discord.Embed(
            title='Команды для администрации и модерации сервера', 
            description=f'Команды для модерации сервера'
        )
        emb2.add_field(
            name = '**Команды**',
            value = f'`{prefix}prefix`\n`{prefix}wlc` или `{prefix}welcome`'
        )
        emb3=discord.Embed(
            title='Команды для развлечения', 
            description=f'Команды для развлечения на сервере'
        )
        emb3.add_field(
            name = '**Команды**',
            value = f'`{prefix}fox`\n`{prefix}dog`\n`{prefix}cat`\n`{prefix}panda`\n`{prefix}redpanda`\n`{prefix}koala`\n`{prefix}wink`\n`{prefix}pat`\n`{prefix}hug`\n`{prefix}memes`'
        )

        embeds=[emb,emb1,emb2,emb3]
        message= await ctx.send(embed= emb)
        page= pag(self.bot, message, only=ctx.author, use_more=False, embeds=embeds, color=0x008000, time_stamp=True)
    
        await page.start()
    
    @help_for_commands.command(name='user', aliases=['userinfo','ui','infouser','iu'])
    async def user_subcommands(self, ctx):

        prefix_1 = prefix_in_guild(self.bot, ctx.message)
        prefix = prefix_1[0]

        user_emb=discord.Embed(
            timestamp= ctx.message.created_at, 
            title=f'Информация про команду: {prefix}user', 
            colour = discord.Color.teal(), 
            description=f'**Команда**: `[user]` или `[userinfo]` или `[infouser]` или `[iu]` или `[ui]`\n**Описание**: показивает информацию про пользователя\n**Использования**: `{prefix}user` или `{prefix}userinfo` или `{prefix}infouser` или `{prefix}iu` или `{prefix}ui`, или если вы хотите узнать информацию о другом пользователя, то после команды пропишите тег пользователя о котором хотите узнать информацию\n**Пример**: `{prefix}user @имя_пользователя`'
        )
        user_emb.set_footer(
            text = ctx.message.author,
            icon_url = ctx.message.author.avatar_url
        )
        await ctx.send(embed=user_emb)

    @help_for_commands.command(name='ping')
    async def pind_subcommands(self,ctx):

        prefix_1 = prefix_in_guild(self.bot, ctx.message)
        prefix = prefix_1[0]

        ping_emb=discord.Embed(
            timestamp= ctx.message.created_at, 
            title=f'Информация про команду: {prefix}ping',
            colour = discord.Color.teal(), 
            description=f'**Команда**: `[ping]`\n**Описание**: показивает пинг бота\n**Использования**: `{prefix}ping`'
        )
        ping_emb.set_footer(
            text=ctx.message.author,
            icon_url = ctx.message.author.avatar_url
        )
        await ctx.send(embed=ping_emb)

    @help_for_commands.command(name='botservers')
    async def botservers_subcommands(self,ctx):

        prefix_1 = prefix_in_guild(self.bot, ctx.message)
        prefix = prefix_1[0]

        botservers_emb=discord.Embed(
            timestamp= ctx.message.created_at,
            title=f'Информация про команду: {prefix}bot_servers', 
            colour = discord.Color.teal(), 
            description=f'**Команда**: `[botservers]`\n**Описание**: показивает на сколько серверах присутствует этот бот\n**Использования**: `{prefix}botservers`'
        )
        botservers_emb.set_footer(
            text = ctx.message.author,
            icon_url = ctx.message.author.avatar_url
        )
        await ctx.send(embed=botservers_emb)   

    @help_for_commands.command(name='tuser')
    async def tuser_subcommands(self,ctx):

        prefix_1 = prefix_in_guild(self.bot, ctx.message)
        prefix = prefix_1[0]

        tuser_emb=discord.Embed(
            title=f'Информация про команду: {prefix}tuser', 
            colour = discord.Color.teal(), 
            description=f'**Команда**: `[tuser]`\n**Описание**: показивает сколько людей используют этого бота\n**Использования**: `{prefix}tuser`'
        )
        tuser_emb.set_footer(
            text = ctx.message.author, 
            icon_url = ctx.message.author.avatar_url
        )
        await ctx.send(
            embed=tuser_emb
        )   

    @help_for_commands.command(name='prefix')
    async def prefix_subcommands(self, ctx):
        
        prefix_1 = prefix_in_guild(self.bot, ctx.message)
        prefix = prefix_1[0]

        prefix_emb=discord.Embed(
            timestamp= ctx.message.created_at, 
            title=f'Информация про команду: {prefix}prefix', 
            colour = discord.Color.teal(), 
            description=f'**Предостережение:** Эту команду может использовать только создатель сервера!\n**Команда**: `[prefix]`\n**Описание**: смена префикса бота на сервере\n**Использования**: `{prefix}prefix *новый префик сервера*`'
        )
        prefix_emb.set_footer(
            text = ctx.message.author,
            icon_url = ctx.message.author.avatar_url
        )
        await ctx.send(embed=prefix_emb) 

    @help_for_commands.command(name='welcome', aliases = ['wlc'])
    async def wlc_subcommands(self, ctx):
        prefix_1 = prefix_in_guild(self.bot, ctx.message)
        prefix = prefix_1[0]

        wlc_emb=discord.Embed(
            timestamp= ctx.message.created_at, 
            title=f'Информация про команду: {prefix}wlc или {prefix}welcome', 
            colour = discord.Color.teal(), 
            description=f'**Предостережение:** Эту команду может использовать только создатель сервера!\n**Команда**: `[wlc]` или `[welcome]`\n**Описание**: установить канал для отправки сообщений о новом юзера сервера\n**Использования**: `{prefix}wlc или {prefix}welcome *ади канала* *true или false*`\n**true** - включить уведомления\n**false** - отключить уведомления\n\n**Пример:** `{prefix}wlc 112215155842828482 true`'
        )
        wlc_emb.set_footer(
            text = ctx.message.author,
            icon_url = ctx.message.author.avatar_url
        )
        await ctx.send(embed=wlc_emb) 

    @help_for_commands.command(name='infobot')
    async def infobot_subcommands(self, ctx):
        prefix_1 = prefix_in_guild(self.bot, ctx.message)
        prefix = prefix_1[0]

        infobot_emb=discord.Embed(
            timestamp= ctx.message.created_at, 
            title=f'Информация про команду: {prefix}infobot', 
            colour = discord.Color.teal(), 
            description=f'**Команда**: `[infobot]`\n**Описание**: показывает информация о боте {self.bot.user.name}\n**Использования**: `{prefix}infobot`'
        )
        infobot_emb.set_footer(
            text = ctx.message.author,
            icon_url = ctx.message.author.avatar_url
        )
        await ctx.send(embed=infobot_emb) 

    @help_for_commands.command(name='serverinfo', aliases = ['si','is'])
    async def serverinfo_subcommands(self, ctx):
        prefix_1 = prefix_in_guild(self.bot, ctx.message)
        prefix = prefix_1[0]

        infobot_emb=discord.Embed(
            timestamp= ctx.message.created_at, 
            title=f'Информация про команду: `{prefix}serverinfo` или `{prefix}si` или `{prefix}is`', 
            colour = discord.Color.teal(), 
            description=f'**Команда**: `[serverinfo]` или `[si]` или `[is]`\n**Описание**: показывает информацию о сервере {ctx.message.guild.name}\n**Использования**: `{prefix}serverinfo` или `{prefix}si` или `{prefix}is`'
        )
        infobot_emb.set_footer(
            text = ctx.message.author,
            icon_url = ctx.message.author.avatar_url
        )
        await ctx.send(embed=infobot_emb) 

def setup(bot):
    bot.add_cog(HelpCommands(bot))
