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
    cursor.execute(f'SELECT prefix_guild FROM public."myBD" WHERE guild_id = \'{guildid}\';')
    prefix = cursor.fetchone()
    conn.commit()
    return prefix

class HelpCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.server = 'Support server Tobi Bot'
        self.server_link = 'https://server-discord.com/743761540758503444'

    @commands.group(name='help',aliases=['helpcmd','i','helpcommands'], invoke_without_command=True)
    async def help_for_commands(self, ctx):
        global prefix 

        prefix_1 = prefix_in_guild(self.bot, ctx.message)
        prefix = prefix_1[0]
        
        emb = discord.Embed(
            title=f'Команды бота {self.bot.user.name}', 
            description=f'Здесь вы узнаете информацию про все команды бота\nНапишите `{prefix}invite` чтобы получить ссылки бота'
        )
        emb.add_field(
            name='**Другая информация**',
            value=f'Чтобы получить больше информации о какой либо команде, вы можете написать: `{prefix}help *команда*` \nТак же, вы можете нажать на реакцию под сообщением, чтобы переключить страницу.\n'
        )
        emb.add_field(
            name = 'Поддержите бота на мониторингах:',
            value = '[{0.server}]({0.server_link})'.format(self),
            inline = False
        )
        emb.set_thumbnail(
            url = 'https://github.com/xzartsust/holo_bot/blob/master/files/image/c8c4113dda8117f63cc993c981f2732d.png?raw=true'
        )
        emb1= discord.Embed(
            title='Команды информации', 
            description=f'Что бы узнать больше о команде напишите `{prefix}help [команда]`. \n**Пример**: `{prefix}help user`'
        )
        emb1.set_thumbnail(
            url = 'https://github.com/xzartsust/holo_bot/blob/master/files/image/c8c4113dda8117f63cc993c981f2732d.png?raw=true'
        )
        emb1.add_field(
            name='**Команды**', 
            value=f'`{prefix}user`\n`{prefix}ping`\n`{prefix}botservers`\n`{prefix}tuser`\n`{prefix}infobot`\n`{prefix}serverinfo` или `{prefix}si` или `{prefix}is`\n`{prefix}serverprefix` или `{prefix}sp` или `{prefix}ps`\n`{prefix}avatar` или `{prefix}av` или `{prefix}a`'
        )
        emb2=discord.Embed(
            title='Команды для администрации и модерации сервера', 
            description=f'Команды для модерации сервера'
        )
        emb2.set_thumbnail(
            url = 'https://github.com/xzartsust/holo_bot/blob/master/files/image/c8c4113dda8117f63cc993c981f2732d.png?raw=true'
        )
        emb2.add_field(
            name = '**Команды**',
            value = f'`{prefix}prefix`\n`{prefix}wlc` или `{prefix}welcome`\n`{prefix}news`\n`{prefix}rwlc`\n`{prefix}mute`\n`{prefix}unmute`\n`{prefix}muterole`\n`{prefix}ban`\n`{prefix}kick`\n`{prefix}unban`\n`{prefix}vote`'
        )
        emb3=discord.Embed(
            title='Команды для развлечения', 
            description=f'Команды для развлечения на сервере'
        )
        emb3.set_thumbnail(
            url = 'https://github.com/xzartsust/holo_bot/blob/master/files/image/c8c4113dda8117f63cc993c981f2732d.png?raw=true'
        )
        emb3.add_field(
            name = '**Команды**',
            value = 'Категории',
            inline = False
        )
        emb3.add_field(
            name = f'**Категория Anime**',
            value = f'`{prefix}wink`\n`{prefix}pat`\n`{prefix}hug`\n`{prefix}neko`\n`{prefix}holo`\n`{prefix}tickle`\n`{prefix}poke`',
            inline = True
        )
        emb3.add_field(
            name = '**Категория Animal**',
            value = f'`{prefix}fox`\n`{prefix}dog`\n`{prefix}cat`\n`{prefix}panda`\n`{prefix}redpanda`\n`{prefix}koala`',
            inline = True
        )
        emb3.add_field(
            name = '**Категория Text**',
            value = f'`{prefix}tcat`'
        )
        emb3.add_field(
            name = f'**Категория Memes**',
            value = f'`{prefix}memes`',
            inline = False
        )
        emb4=discord.Embed(
            title = 'NSFW команды',
            description = 'Эти команды можно использовать только в чате где включен режим **NSFW**'
        )
        emb4.add_field(
            name = '**Команды**',
            value = 'Категории',
            inline = False
        )
        emb4.add_field(
            name = '**Holo**',
            value = f'`{prefix}hololewd`\n`{prefix}holoero`',
            inline = True
        )
        emb4.set_thumbnail(
            url = 'https://github.com/xzartsust/holo_bot/blob/master/files/image/c8c4113dda8117f63cc993c981f2732d.png?raw=true'
        )
        emb4.add_field(
            name = '**Neko**',
            value = f'`{prefix}nekolewd`\n`{prefix}nekogif`\n`{prefix}lewdkemo`\n`{prefix}erokemo`\n`{prefix}kitsunero`\n`{prefix}kitsunelewd`',
            inline = True
        )
        emb4.add_field(
            name = '**Anime**',
            value = f'`{prefix}aniero`\n`{prefix}classic`\n`{prefix}keta`\n`{prefix}les`'
        )

        emb_music = discord.Embed(
            title = 'Музыкальные команды :musical_note: :musical_note: :musical_note:',
            description = f'**Внимание:** Музыкальные команды находятся в доработке, и иногда можут некоректно работать!\nЕсли у вас возникли какие-то вопросы по поводу этого то вы можете использовать команду `{prefix}help music`, написать в личку моему создателю или оставить этот вопрос на **Support server Tobi Bot**'
        )
        emb_music.add_field(
            name = '**Команды**',
            value = f'`{prefix}play` или `{prefix}pla` или `{prefix}p` \n`{prefix}join` или `{prefix}j`\n`{prefix}leave` или `{prefix}lea` или `{prefix}l`\n`{prefix}pause` или `{prefix}pau` или `{prefix}p`\n`{prefix}resume` или `{prefix}res` или `{prefix}r`\n`{prefix}stop` или `{prefix}st` или `{prefix}s`'
        )

        embeds=[emb,emb1,emb2,emb3,emb4, emb_music]
        message= await ctx.send(embed = emb)
        page= pag(self.bot, message, only = ctx.author, use_more = False, embeds = embeds, color = 0x008000, time_stamp = True)
    
        await page.start()
    
    @help_for_commands.command(name = 'user', aliases=['userinfo','ui','infouser','iu'])
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

    @help_for_commands.command(name = 'ping')
    async def pind_subcommands(self, ctx):

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

    @help_for_commands.command(name = 'botservers')
    async def botservers_subcommands(self, ctx):

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

    @help_for_commands.command(name = 'tuser')
    async def tuser_subcommands(self, ctx):

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

    @help_for_commands.command(name = 'prefix')
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

    @help_for_commands.command(name = 'welcome', aliases = ['wlc'])
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

    @help_for_commands.command(name = 'infobot')
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

    @help_for_commands.command(name = 'serverinfo', aliases = ['si','is'])
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
    
    @help_for_commands.command(name = 'prefixserver', aliases = ['sp','ps'])
    async def prefixserver_subcommands(self, ctx):
        prefix_1 = prefix_in_guild(self.bot, ctx.message)
        prefix = prefix_1[0]

        ps_emb=discord.Embed(
            timestamp= ctx.message.created_at, 
            title=f'Информация про команду: `{prefix}serverprefix` или `{prefix}sp` или `{prefix}ps`', 
            colour = discord.Color.teal(), 
            description=f'**Команда**: `[serverprefix]` или `[sp]` или `[ps]`\n**Описание**: показывает текущий префикс сервера {ctx.message.guild.name}\n**Использования**: `{prefix}serverprefix` или `{prefix}sp` или `{prefix}ps`'
        )
        ps_emb.set_footer(
            text = ctx.message.author,
            icon_url = ctx.message.author.avatar_url
        )
        await ctx.send(embed=ps_emb) 

    @help_for_commands.command(name = 'news')
    async def news_subcommands(self, ctx):
        prefix_1 = prefix_in_guild(self.bot, ctx.message)
        prefix = prefix_1[0]

        news_emb=discord.Embed(
            timestamp= ctx.message.created_at, 
            title=f'Информация про команду: `{prefix}news`', 
            colour = discord.Color.teal(), 
            description=f'**Команда**: `[news]`\n**Описание**: создает на сервере новость\n**Использования**: `{prefix}news *айди канала или тег канала* *\"заголовок\"* *текст новости*`\n\n**Пример:** `{prefix}news 124555785215 \"Новость сервера!\" Просто пример`\n\n**Внимание!**\nЗаголовок должнен быть обязательно в двойных кавычках, также у юзера который использует эту команду, в его роли должна быть включена функция управления сообщениями (manage messages)'
        )
        news_emb.set_footer(
            text = ctx.message.author,
            icon_url = ctx.message.author.avatar_url
        )
        await ctx.send(embed=news_emb) 

    @help_for_commands.command(name = 'rwlc')
    async def rwlc_subcommands(self, ctx):
        prefix_1 = prefix_in_guild(self.bot, ctx.message)
        prefix = prefix_1[0]

        rwlc_emb=discord.Embed(
            timestamp= ctx.message.created_at, 
            title=f'Информация про команду: `{prefix}rwlc`', 
            colour = discord.Color.teal(), 
            description=f'**Предостережение:** Эту команду может использовать только создатель сервера!\n**Команда**: `[rwlc]`\n**Описание**: установить роль которая будет выдаваться новим пользователям сервера\n**Использования**: `{prefix}rwlc *ади роли* *true или false*`\n**true** - включить автовидачу роли\n**false** - отключить автовидачу роли\n\n**Пример:** `{prefix}rwlc 112215155842828482 true`'
        )
        rwlc_emb.set_footer(
            text = ctx.message.author,
            icon_url = ctx.message.author.avatar_url
        )
        await ctx.send(embed=rwlc_emb)
    
    @help_for_commands.command(name = 'mute')
    async def mute_subcommands(self, ctx):
        prefix_1 = prefix_in_guild(self.bot, ctx.message)
        prefix = prefix_1[0]

        mute_emb=discord.Embed(
            timestamp= ctx.message.created_at, 
            title=f'Информация про команду: `{prefix}mute`', 
            colour = discord.Color.teal(), 
            description=f'**Предостережение:** Эту команду можут использовать роли в которых есть права **Выгонять участников**!\n**Команда**: `[mute]`\n**Описание**: выдает безмолвия участнику сервера\n**Использования**: `{prefix}mute *кому* *причина*`\n\n\n**Пример:** `{prefix}mute [@тег_или_имя_пользователя] [reason]`'
        )
        mute_emb.set_footer(
            text = ctx.message.author,
            icon_url = ctx.message.author.avatar_url
        )
        await ctx.send(embed=mute_emb)

    @help_for_commands.command(name = 'muterole')
    async def muterole_subcommands(self, ctx):
        prefix_1 = prefix_in_guild(self.bot, ctx.message)
        prefix = prefix_1[0]

        muterole_emb=discord.Embed(
            timestamp= ctx.message.created_at, 
            title=f'Информация про команду: `{prefix}muterole`', 
            colour = discord.Color.teal(), 
            description=f'**Предостережение:** Эту команду может использовать только создатель сервера!\n**Команда**: `[muterole]`\n**Описание**: установить роль которая будет выдаваться по команде `mute`\n**Использования**: `{prefix}muterole *ади роли*`\n\n**Пример:** `{prefix}muterole [id role]`'
            )
        muterole_emb.set_footer(
            text = ctx.message.author,
            icon_url = ctx.message.author.avatar_url
            )
        await ctx.send(embed=muterole_emb)
    
    @help_for_commands.command(name = 'ban')
    async def ban_subcommands(self, ctx):
        prefix_1 = prefix_in_guild(self.bot, ctx.message)
        prefix = prefix_1[0]

        ban_emb=discord.Embed(
            timestamp= ctx.message.created_at, 
            title=f'Информация про команду: `{prefix}ban`', 
            colour = discord.Color.teal(), 
            description=f'**Предостережение:** Эту команду можут использовать роли в которых есть права **Ban Members**!\n**Команда**: `[ban]`\n**Описание**: Заблокировать пользователя на сервере\n**Использования**: `{prefix}ban *кому* *reason*`\n reason - может быть пустым\n\n**Пример:** `{prefix}ban @Member spam bot`\n\n**Внимание:** Можно сразу несколько пользователей\n**Пример:** `{prefix}ban @Member @Member2 *reson*`'
            )
        ban_emb.set_footer(
            text = ctx.message.author,
            icon_url = ctx.message.author.avatar_url
            )
        await ctx.send(embed=ban_emb)

    @help_for_commands.command(name = 'play')
    async def play_subcommands(self, ctx):
        prefix_1 = prefix_in_guild(self.bot, ctx.message)
        prefix = prefix_1[0]

        play_emb=discord.Embed(
            timestamp= ctx.message.created_at, 
            title=f'Информация про команду: {prefix}play или {prefix}pl или {prefix}p', 
            colour = discord.Color.teal(), 
            description=f'**Предостережение:** Пока что нельзя добавлять музыку в очередь сначала нужно зачикаты пока доиграет одна музыка после этого добавлять новую ссылку на новую музыку, более подробно в команде `{prefix}help music`\n\n**Команда**: `[play]`\n**Описание**: проиграть музику\n**Использования**: `{prefix}play *силка на музыку*`\n\n**Пример:** `{prefix}play https://www.youtube.com/watch?v=9sjWU5dGcGI`'
            )
        play_emb.set_footer(
            text = ctx.message.author,
            icon_url = ctx.message.author.avatar_url
            )
        await ctx.send(embed=play_emb)

    @help_for_commands.command(name = 'join')
    async def join_subcommands(self, ctx):

        prefix_1 = prefix_in_guild(self.bot, ctx.message)
        prefix = prefix_1[0]

        join_emb=discord.Embed(
            title=f'Информация про команду: {prefix}join или {prefix}j', 
            colour = discord.Color.teal(), 
            description=f'**Команда**: `[join]`\n**Описание**: добавить бота в голосовой канал\n**Использования**: `{prefix}join`'
        )
        join_emb.set_footer(
            text = ctx.message.author, 
            icon_url = ctx.message.author.avatar_url
        )
        await ctx.send(embed=join_emb)

    @help_for_commands.command(name = 'leave')
    async def leave_subcommands(self, ctx):

        prefix_1 = prefix_in_guild(self.bot, ctx.message)
        prefix = prefix_1[0]

        leave_emb=discord.Embed(
            title=f'Информация про команду: {prefix}leave или {prefix}lea или {prefix}l', 
            colour = discord.Color.teal(), 
            description=f'**Команда**: `[leave]`\n**Описание**: выгнать бота с голосового канала\n**Использования**: `{prefix}leave`'
        )
        leave_emb.set_footer(
            text = ctx.message.author, 
            icon_url = ctx.message.author.avatar_url
        )
        await ctx.send(
            embed = leave_emb
        )      

    @help_for_commands.command(name = 'pause')
    async def pause_subcommands(self, ctx):

        prefix_1 = prefix_in_guild(self.bot, ctx.message)
        prefix = prefix_1[0]

        pause_emb=discord.Embed(
            title=f'Информация про команду: {prefix}pause или {prefix}pau или {prefix}pa', 
            colour = discord.Color.teal(), 
            description=f'**Команда**: `[pause]`\n**Описание**: поставить текущую песню на паузу\n**Использования**: `{prefix}pause`'
        )
        pause_emb.set_footer(
            text = ctx.message.author, 
            icon_url = ctx.message.author.avatar_url
        )
        await ctx.send(
            embed = pause_emb
        )   

    @help_for_commands.command(name = 'resume')
    async def resume_subcommands(self, ctx):

        prefix_1 = prefix_in_guild(self.bot, ctx.message)
        prefix = prefix_1[0]

        resume_emb=discord.Embed(
            title = f'Информация про команду: {prefix}resume или {prefix}res или {prefix}r', 
            colour = discord.Color.teal(), 
            description = f'**Команда**: `[resume]`\n**Описание**: возобновить воспроизведение музыки\n**Использования**: `{prefix}resume`'
        )
        resume_emb.set_footer(
            text = ctx.message.author, 
            icon_url = ctx.message.author.avatar_url
        )
        await ctx.send(
            embed = resume_emb
        )
     
    @help_for_commands.command(name = 'stop')
    async def stop_subcommands(self, ctx):

        prefix_1 = prefix_in_guild(self.bot, ctx.message)
        prefix = prefix_1[0]

        stop_emb = discord.Embed(
            title=f'Информация про команду: {prefix}stop или {prefix}st или {prefix}s', 
            colour = discord.Color.teal(), 
            description=f'**Команда**: `[stop]`\n**Описание**: закончить воспроизведения музыки\n**Использования**: `{prefix}stop`'
        )
        stop_emb.set_footer(
            text = ctx.message.author, 
            icon_url = ctx.message.author.avatar_url
        )
        await ctx.send(
            embed = stop_emb
        )   

    @help_for_commands.command(name='music')
    async def music_subcommands(self, ctx):

        prefix_1 = prefix_in_guild(self.bot, ctx.message)
        prefix = prefix_1[0]

        await ctx.send(f'```Как использовать музыкальные команды?```\nСначала вы присоединяете командой `{prefix}join` бота к себе в войс, после этого командой `{prefix}play [Сылка на музыку] или [назва музыки]` запускаете воспроизведения музыки.\n\n**Внимание** пока что нельзя добавлять несколько песен сразу (эта функция в доработке), вы сможете задать следующие песню только после того как закончится и играющая на данный момент или после команды `{prefix}stop`.\n\nПожалуйста будьте внимательны с этим.')

    @help_for_commands.command(name = 'kick')
    async def kick_subcommands(self, ctx):
        prefix_1 = prefix_in_guild(self.bot, ctx.message)
        prefix = prefix_1[0]

        ban_emb=discord.Embed(
            timestamp= ctx.message.created_at, 
            title=f'Информация про команду: `{prefix}kick`', 
            colour = discord.Color.teal(), 
            description=f'**Предостережение:** Эту команду можут использовать роли в которых есть права **Kick Members**!\n**Команда**: `[kick]`\n**Описание**: Выгнать пользователя из сервере\n**Использования**: `{prefix}kick *кому* *reason*`\n reason - может быть пустым\n\n**Пример:** `{prefix}kick @Member spam bot`'
            )
        ban_emb.set_footer(
            text = ctx.message.author,
            icon_url = ctx.message.author.avatar_url
            )
        await ctx.send(embed=ban_emb)

    @help_for_commands.command(name = 'unban')
    async def unban_subcommands(self, ctx):
        prefix_1 = prefix_in_guild(self.bot, ctx.message)
        prefix = prefix_1[0]

        unban_emb=discord.Embed(
            timestamp= ctx.message.created_at, 
            title=f'Информация про команду: `{prefix}unban`', 
            colour = discord.Color.teal(), 
            description=f'**Предостережение:** Эту команду можут использовать роли в которых есть права **Ban Members**!\n**Команда**: `[ban]`\n**Описание**: Разблокировать пользователя на сервере\n**Использования**: `{prefix}ban *кого*`\n\n**Пример:** `{prefix}ban Test Account#2125`'
            )
        unban_emb.set_footer(
            text = ctx.message.author,
            icon_url = ctx.message.author.avatar_url
            )
        await ctx.send(embed = unban_emb)

    @help_for_commands.command(name = 'vote')
    async def vote_subcommands(self, ctx):
        prefix_1 = prefix_in_guild(self.bot, ctx.message)
        prefix = prefix_1[0]

        vote_emb=discord.Embed(
            timestamp = ctx.message.created_at, 
            title = f'Информация про команду: `{prefix}vote`', 
            colour = discord.Color.teal(), 
            description = f'**Команда**: `[vote]`\n**Описание**: создает голосование на сервере\n**Использования**: `{prefix}vote *\"тема голосования\"* \"*текст*\" [cылка на картинку]`\n\n**Пример:** `{prefix}vote \"Голосования!\" \"О чем голосуем?\" https://raw.githubusercontent.com/xzartsust/Tobi-Bot/master/files/image/c8c4113dda8117f63cc993c981f2732d.png`\nМожно использовать без картинки\n\n**Внимание!**\n**Тема голосование** и **Текст** должны быть обязательно в двойных кавычках, также у юзера который использует эту команду, в его роли должна быть включена функция управления сообщениями (manage messages)'
        )
        vote_emb.set_footer(
            text = ctx.message.author,
            icon_url = ctx.message.author.avatar_url
        )
        await ctx.send(embed = vote_emb) 

    @help_for_commands.command(name = 'unmute')
    async def unmute_subcommands(self, ctx):
        prefix_1 = prefix_in_guild(self.bot, ctx.message)
        prefix = prefix_1[0]

        unmute_emb = discord.Embed(
            timestamp= ctx.message.created_at, 
            title=f'Информация про команду: `{prefix}unmute`', 
            colour = discord.Color.teal(), 
            description=f'**Предостережение:** Эту команду можут использовать роли в которых есть права **Выгонять участников**!\n**Команда**: `[unmute]`\n**Описание**: снимает безмолвия с участника сервера\n**Использования**: `{prefix}unmute *кого*`\n\n\n**Пример:** `{prefix}mute [@тег_или_имя_пользователя]`'
        )
        unmute_emb.set_footer(
            text = ctx.message.author,
            icon_url = ctx.message.author.avatar_url
        )
        await ctx.send(embed = unmute_emb)

def setup(bot):
    bot.add_cog(HelpCommands(bot))
