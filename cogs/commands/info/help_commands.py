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


def prefix_in_guild(bot, message):
    guildid = message.guild.id
    try:
        conn = psycopg2.connect(
            database = f"{database}", 
            user = f"{user}", 
            password = f"{password}", 
            host = f"{host}", 
            port = "5432"
        )
        cursor = conn.cursor()
        cursor.execute(f'SELECT prefix_guild FROM public."myBD" WHERE guild_id = \'{guildid}\';')
        prefix = cursor.fetchone()
        conn.commit()
    finally:
            if(conn):
                cursor.close()
                conn.close()
                
    return prefix

class HelpCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.server = 'Support server Tobi Bot(server-discord)'
        self.server_2 = 'Support server Tobi Bot(top.gg)'
        self.server_link = 'https://server-discord.com/743761540758503444'
        self.server_link_2 = 'https://top.gg/servers/743761540758503444'


    @commands.group(name='help',aliases=['helpcmd','i','helpcommands'], invoke_without_command=True)
    async def help_for_commands(self, ctx):
        global prefix 

        prefix_1 = prefix_in_guild(self.bot, ctx.message)
        prefix = prefix_1[0]
        
        start = discord.Embed(
            title=f'Команды бота {self.bot.user.name}', 
            description=f'Здесь вы узнаете информацию про все команды бота\nНапишите `{prefix}invite` чтобы получить ссылки бота'
        )
        start.add_field(
            name='**Другая информация**',
            value=f'Чтобы получить больше информации о какой либо команде, вы можете написать: `{prefix}help *команда*` \nТак же, вы можете нажать на реакцию под сообщением, чтобы переключить страницу.\n'
        )
        start.add_field(
            name = 'Поддержите Suport sever бота на мониторингах:',
            value = '[{0.server}]({0.server_link})\n[{0.server_2}]({0.server_link_2})'.format(self),
            inline = False
        )
        start.set_thumbnail(
            url = 'https://github.com/xzartsust/holo_bot/blob/master/files/image/c8c4113dda8117f63cc993c981f2732d.png?raw=true'
        )
        information = discord.Embed(
            title='Команды информации', 
            description=f'Что бы узнать больше о команде напишите `{prefix}help [команда]`. \n**Пример**: `{prefix}help user`'
        )
        information.set_thumbnail(
            url = 'https://github.com/xzartsust/holo_bot/blob/master/files/image/c8c4113dda8117f63cc993c981f2732d.png?raw=true'
        )
        information.add_field(
            name='**Команды**', 
            value=f'`{prefix}user`\n`{prefix}infobot`\n`{prefix}serverinfo` или `{prefix}si` или `{prefix}is`\n`{prefix}serverprefix` или `{prefix}sp` или `{prefix}ps`\n`{prefix}avatar` или `{prefix}av` или `{prefix}a`'
        )
        Moder = discord.Embed(
            title='Команды для администрации и модерации сервера', 
            description=f'Команды для модерации сервера'
        )
        Moder.set_thumbnail(
            url = 'https://github.com/xzartsust/holo_bot/blob/master/files/image/c8c4113dda8117f63cc993c981f2732d.png?raw=true'
        )
        Moder.add_field(
            name = '**Команды**',
            value = f'`{prefix}prefix`\n`{prefix}news`\n`{prefix}vote`\n`{prefix}rwlc`\n`{prefix}muterole`\n`{prefix}send`'
        )
        Moder.add_field(
            name = '**Команды для действий с пользователями**',
            value = f'`{prefix}ban`\n`{prefix}unban`\n`{prefix}mute`\n`{prefix}unmute`\n`{prefix}kick`'
        )

        diferend_photo = discord.Embed(
            title='Команды для развлечения', 
            description=f'Команды для развлечения на сервере'
        )
        diferend_photo.set_thumbnail(
            url = 'https://github.com/xzartsust/holo_bot/blob/master/files/image/c8c4113dda8117f63cc993c981f2732d.png?raw=true'
        )
        diferend_photo.add_field(
            name = '**Команды**',
            value = 'Категории',
            inline = False
        )
        diferend_photo.add_field(
            name = f'**Категория Anime**',
            value = f'`{prefix}wink`\n`{prefix}pat`\n`{prefix}hug`\n`{prefix}neko`\n`{prefix}holo`\n`{prefix}tickle`\n`{prefix}poke`',
            inline = True
        )
        diferend_photo.add_field(
            name = '**Категория Animal**',
            value = f'`{prefix}fox`\n`{prefix}dog`\n`{prefix}cat`\n`{prefix}panda`\n`{prefix}redpanda`\n`{prefix}koala`',
            inline = True
        )
        diferend_photo.add_field(
            name = '**Категория Text**',
            value = f'`{prefix}tcat`'
        )
        diferend_photo.add_field(
            name = f'**Категория Memes**',
            value = f'`{prefix}memes`',
            inline = False
        )

        NSFW_emb = discord.Embed(
            title = 'NSFW команды',
            description = 'Эти команды можно использовать только в чате где включен режим **NSFW**'
        )
        NSFW_emb.add_field(
            name = '**Команды**',
            value = 'Категории',
            inline = False
        )
        NSFW_emb.add_field(
            name = '**Holo**',
            value = f'`{prefix}hololewd`\n`{prefix}holoero`',
            inline = True
        )
        NSFW_emb.set_thumbnail(
            url = 'https://github.com/xzartsust/holo_bot/blob/master/files/image/c8c4113dda8117f63cc993c981f2732d.png?raw=true'
        )
        NSFW_emb.add_field(
            name = '**Neko**',
            value = f'`{prefix}nekolewd`\n`{prefix}nekogif`\n`{prefix}lewdkemo`\n`{prefix}erokemo`\n`{prefix}kitsunero`\n`{prefix}kitsunelewd`',
            inline = True
        )
        NSFW_emb.add_field(
            name = '**Anime**',
            value = f'`{prefix}aniero`\n`{prefix}classic`\n`{prefix}keta`\n`{prefix}les`'
        )

        emb_music = discord.Embed(
            title = ':musical_note: :musical_note: Музыкальные команды :musical_note: :musical_note:',
            description = f'Если у вас возникли какие-то вопросы по поводу этого то вы можете написать в личку моему создателю или оставить этот вопрос на **Support server Tobi Bot**'
        )
        emb_music.set_thumbnail(
            url = 'https://github.com/xzartsust/Tobi-Bot/blob/master/files/image/c8c4113dda8117f63cc993c981f2732d.png?raw=true'
        )
        emb_music.add_field(
            name = '**Команды**',
            value = f'`{prefix}play` или `{prefix}pl` или `{prefix}p` \n`{prefix}pause` или `{prefix}pa` или `{prefix}pau` \n`{prefix}resume` или `{prefix}res` или `{prefix}r` \n`{prefix}stop` или `{prefix}st` или `{prefix}s` \n`{prefix}join` или `{prefix}jo` или `{prefix}j` \n`{prefix}leave` или `{prefix}lea` или `{prefix}l` или `{prefix}disconnect`  \n`{prefix}summon` или `{prefix}sum` или `{prefix}summ` \n`{prefix}now` или `{prefix}current` или `{prefix}playing` \n`{prefix}skip` или `{prefix}sk` \n`{prefix}queue` или `{prefix}qu` или `{prefix}q` \n`{prefix}shuffle` или `{prefix}shu` или `{prefix}sh` или `{prefix}shake` \n`{prefix}remove` или `{prefix}re` или `{prefix}rem`'
        )

        welcome_emb = discord.Embed(
            title = 'Команди для приветствия новых пользователей',
            description = 'Теперь можно делать кастомной текст для приветствия\n\nКоманды с раздела *Команды для установки текста поздравления нового пользователя на сервере* можут посмотреть как использовать, роли в которых есть права **Управлять Сервером**!',
        )
        welcome_emb.add_field(
            name = '**Команды для установление канала**',
            value = f'`{prefix}wlc` или `{prefix}welcome`',
        )
        welcome_emb.add_field(
            name = '**Команды для установки текста поздравления нового пользователя на сервере**',
            value = f'`{prefix}wtitle`\n`{prefix}wdescript`\n`{prefix}wfooter`',
            inline = True
        )
        welcome_emb.set_thumbnail(
            url = 'https://github.com/xzartsust/Tobi-Bot/blob/master/files/image/c8c4113dda8117f63cc993c981f2732d.png?raw=true'
        )
        welcome_emb.set_image(
            url = 'https://github.com/xzartsust/Tobi-Bot/blob/master/files/image/help_welcome.jpg?raw=true'
        )

        warn_embed = discord.Embed(
            title = 'Warn команды',
            description = 'Тeперь у бота есть **warn** система\n\nКоманды с раздела *Warn команды* можут посмотреть как использовать, роли в которых есть права **Управлять Сервером**!'
        )
        warn_embed.set_thumbnail(
            url = 'https://github.com/xzartsust/Tobi-Bot/blob/master/files/image/c8c4113dda8117f63cc993c981f2732d.png?raw=true'
        )
        warn_embed.add_field(
            name = '**Команды**',
            value = f'`{prefix}warn`\n`{prefix}mwarn`\n`{prefix}resetwarn`'
        )

        privat_channel_embed = discord.Embed(
            title = 'Прививатные голосовие канали',
            description = '''
            Команды с раздела *Команды* могут использовать те кто имеют права **Администратора**
            ''')
        privat_channel_embed.set_thumbnail(url = 'https://github.com/xzartsust/Tobi-Bot/blob/master/files/image/c8c4113dda8117f63cc993c981f2732d.png?raw=true')
        privat_channel_embed.add_field(
            name = 'Команды',
            value = f'''
            `{prefix}privatchnl`
            `{prefix}resetprivchannel`''')
        
        report_system_embed = discord.Embed(
            title = 'Репорт система',
            description = f'''
            **Внимания!!!** Использувать команду `{prefix}report` Можно каждые 6 часов
            ''')
        report_system_embed.set_thumbnail(url = 'https://github.com/xzartsust/Tobi-Bot/blob/master/files/image/c8c4113dda8117f63cc993c981f2732d.png?raw=true')
        report_system_embed.add_field(
            name = 'Команды',
            value = f'''
            `{prefix}report`
            `{prefix}reportchannel`''')

        embeds = [start, information, Moder, warn_embed, report_system_embed, privat_channel_embed, welcome_emb, diferend_photo, NSFW_emb]
        message = await ctx.send(embed = start)
        page = pag(self.bot, message, only = ctx.author, use_more = False, embeds = embeds, color = 0x008000, time_stamp = True)
    
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
            description=f'**Предостережение:** Эту команду можут использовать роли в которых есть права **Банить участников**!\n**Команда**: `[ban]`\n**Описание**: Заблокировать пользователя на сервере\n**Использования**: `{prefix}ban *кому* *reason*`\n reason - может быть пустым\n\n**Пример:** `{prefix}ban @Member spam bot`\n\n**Внимание:** Можно сразу несколько пользователей\n**Пример:** `{prefix}ban @Member @Member2 *reson*`'
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
            description=f'**Команда**: `[play]`\n**Описание**: проиграть музику\n**Использования**: `{prefix}play *силка_на_музыку_назва_музыки*`\n\n**Пример:** `{prefix}play https://www.youtube.com/watch?v=9sjWU5dGcGI`'
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
            title=f'Информация про команду: {prefix}join или {prefix}jo или {prefix}j', 
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
            title=f'Информация про команду: {prefix}leave или {prefix}lea или {prefix}l или {prefix}disconnect', 
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

    @help_for_commands.command(name = 'kick')
    async def kick_subcommands(self, ctx):
        prefix_1 = prefix_in_guild(self.bot, ctx.message)
        prefix = prefix_1[0]

        ban_emb=discord.Embed(
            timestamp= ctx.message.created_at, 
            title=f'Информация про команду: `{prefix}kick`', 
            colour = discord.Color.teal(), 
            description=f'**Предостережение:** Эту команду можут использовать роли в которых есть права **Выгонять участников**!\n**Команда**: `[kick]`\n**Описание**: Выгнать пользователя из сервере\n**Использования**: `{prefix}kick *кому* *reason*`\n reason - может быть пустым\n\n**Пример:** `{prefix}kick @Member spam bot`'
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
            description=f'**Предостережение:** Эту команду можут использовать роли в которых есть права **Банить участников**!\n**Команда**: `[ban]`\n**Описание**: Разблокировать пользователя на сервере\n**Использования**: `{prefix}ban *кого*`\n\n**Пример:** `{prefix}ban Test Account#2125`'
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
            description = f'**Команда**: `[vote]`\n**Предостережение:** Эту команду можут использовать роли в которых есть права **Управлять сообщениями**!\n\n**Описание**: создает голосование на сервере\n**Использования**: `{prefix}vote *\"тема голосования\"* \"*текст*\" [cылка на картинку]`\n\n**Пример:** `{prefix}vote \"Голосования!\" \"О чем голосуем?\" https://raw.githubusercontent.com/xzartsust/Tobi-Bot/master/files/image/c8c4113dda8117f63cc993c981f2732d.png`\nМожно использовать без картинки\n\n**Внимание!**\n**Тема голосование** и **Текст** должны быть обязательно в двойных кавычках, также у юзера который использует эту команду, в его роли должна быть включена функция управления сообщениями (manage messages)'
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

    @help_for_commands.command(name = 'summon')
    async def summon_subcommands(self, ctx):

        prefix_1 = prefix_in_guild(self.bot, ctx.message)
        prefix = prefix_1[0]

        summon_emb = discord.Embed(
            title=f'Информация про команду: {prefix}summon или {prefix}sum или {prefix}summ', 
            colour = discord.Color.teal(), 
            description=f'**Команда**: `[summon]`\n**Предостережение:** Эту команду можут использовать роли в которых есть права **Администратор и Управлять сервером**!\n\n**Описание**: Перетянуть бота в другой голосвой канал\n**Использования**: `{prefix}summon`'
        )
        summon_emb.set_footer(
            text = ctx.message.author, 
            icon_url = ctx.message.author.avatar_url
        )
        await ctx.send(
            embed = summon_emb
        ) 

    @help_for_commands.command(name = 'now')
    async def now_subcommands(self, ctx):

        prefix_1 = prefix_in_guild(self.bot, ctx.message)
        prefix = prefix_1[0]

        now_emb = discord.Embed(
            title=f'Информация про команду: {prefix}now или {prefix}current или {prefix}playing', 
            colour = discord.Color.teal(), 
            description=f'**Команда**: `[now]`\n**Описание**: посмотреть какая музыка сейчас играет\n**Использования**: `{prefix}now`'
        )
        now_emb.set_footer(
            text = ctx.message.author, 
            icon_url = ctx.message.author.avatar_url
        )
        await ctx.send(
            embed = now_emb
        ) 

    @help_for_commands.command(name = 'skip')
    async def skip_subcommands(self, ctx):

        prefix_1 = prefix_in_guild(self.bot, ctx.message)
        prefix = prefix_1[0]

        skip_emb = discord.Embed(
            title=f'Информация про команду: {prefix}skip или {prefix}sk', 
            colour = discord.Color.teal(), 
            description=f'**Команда**: `[skip]`\n**Описание**: пропустить текущую музыку\n**Использования**: `{prefix}skip`'
        )
        skip_emb.set_footer(
            text = ctx.message.author, 
            icon_url = ctx.message.author.avatar_url
        )
        await ctx.send(
            embed = skip_emb
        ) 

    @help_for_commands.command(name = 'queue')
    async def queue_subcommands(self, ctx):

        prefix_1 = prefix_in_guild(self.bot, ctx.message)
        prefix = prefix_1[0]

        queue_emb = discord.Embed(
            title=f'Информация про команду: {prefix}queue или {prefix}qu или {prefix}q', 
            colour = discord.Color.teal(), 
            description=f'**Команда**: `[queue]`\n**Описание**: посмотреть очередь\n**Использования**: `{prefix}queue`'
        )
        queue_emb.set_footer(
            text = ctx.message.author, 
            icon_url = ctx.message.author.avatar_url
        )
        await ctx.send(
            embed = queue_emb
        ) 

    @help_for_commands.command(name = 'shuffle')
    async def shuffle_subcommands(self, ctx):

        prefix_1 = prefix_in_guild(self.bot, ctx.message)
        prefix = prefix_1[0]

        shuffle_emb = discord.Embed(
            title=f'Информация про команду: {prefix}shuffle или {prefix}shu или {prefix}sh или {prefix}shake', 
            colour = discord.Color.teal(), 
            description=f'**Команда**: `[shuffle]`\n**Описание**: перемешать музыку в очереди\n**Использования**: `{prefix}shuffle`'
        )
        shuffle_emb.set_footer(
            text = ctx.message.author, 
            icon_url = ctx.message.author.avatar_url
        )
        await ctx.send(
            embed = shuffle_emb
        ) 

    @help_for_commands.command(name = 'remove')
    async def remove_subcommands(self, ctx):

        prefix_1 = prefix_in_guild(self.bot, ctx.message)
        prefix = prefix_1[0]

        remove_emb = discord.Embed(
            title=f'Информация про команду: {prefix}remove или {prefix}rem или {prefix}re', 
            colour = discord.Color.teal(), 
            description=f'**Команда**: `[remove]`\n**Описание**: удалить музыку с очереди\n**Использования**: `{prefix}remove [номер музыки]`'
        )
        remove_emb.set_footer(
            text = ctx.message.author, 
            icon_url = ctx.message.author.avatar_url
        )
        remove_emb.set_image(
            url = 'https://github.com/xzartsust/Tobi-Bot/blob/master/files/image/Screenshot_2.png?raw=true'
        )
        await ctx.send(
            embed = remove_emb
        ) 



    @help_for_commands.command(name = 'help_welcome')
    @commands.has_permissions(manage_guild = True)
    async def help_welcome_subcommands(self, ctx):

        description_defolt = 'Каждый участник этого сервере равен перед другими. Поэтому настоятельно просим ознакомиться с правилами сервера\nЗаранее благодарим Вас за вежливость и адекватность.'

        help_welcome = discord.Embed(
            title = f'Приветствуем Вас на {ctx.guild.name}!',
            description = f'{description_defolt}',
            colour = discord.Color.green()
        )
        help_welcome.set_thumbnail(
            url = ctx.message.author.avatar_url
        )
        help_welcome.set_footer(
            text = f'{ctx.message.author.id}' + ' | Приятного времяпрепровождения!',
            icon_url= 'https://github.com/xzartsust/holo_bot/blob/master/files/image/id.png?raw=true'
        )
        await ctx.send(f'Дефолтне приветствие\n{ctx.message.author.mention}', embed = help_welcome)

    @help_for_commands.command(name = 'wtitle')
    @commands.has_permissions(manage_guild = True)
    async def wtitle_emb_subcommands(self, ctx):

        prefix_1 = prefix_in_guild(self.bot, ctx.message)
        prefix = prefix_1[0]

        wtitle_emb = discord.Embed(
            title=f'Информация про команду: {prefix}wtitle', 
            colour = discord.Color.teal(), 
            description=f'**Команда**: `[wtitle]`\n**Описание**: установить заголовок приветствия\n**Использования**: `{prefix}wtitle [текст]`\n\n**Пример:** `{prefix}wtitle Приветствую тебя на сервере`'
        )
        wtitle_emb.set_footer(
            text = ctx.message.author, 
            icon_url = ctx.message.author.avatar_url
        )
        wtitle_emb.set_image(
            url = 'https://github.com/xzartsust/Tobi-Bot/blob/master/files/image/title.png?raw=true'
        )
        await ctx.send(
            embed = wtitle_emb
        ) 

    @help_for_commands.command(name = 'wdescript')
    @commands.has_permissions(manage_guild = True)
    async def wdescript_subcommands(self, ctx):

        prefix_1 = prefix_in_guild(self.bot, ctx.message)
        prefix = prefix_1[0]

        wdescript = discord.Embed(
            title=f'Информация про команду: {prefix}wdescript', 
            colour = discord.Color.teal(), 
            description=f'**Команда**: `[wdescript]`\n**Описание**: установить главный текст приветствия\n**Использования**: `{prefix}wdescript [текст]`\n\n**Пример**: `{prefix}wtitle Прочтите правила сервера пожалуйста и всего вам хорошего`'
        )
        wdescript.set_footer(
            text = ctx.message.author, 
            icon_url = ctx.message.author.avatar_url
        )
        wdescript.set_image(
            url = 'https://github.com/xzartsust/Tobi-Bot/blob/master/files/image/description.png?raw=true'
        )
        await ctx.send(
            embed = wdescript
        ) 

    @help_for_commands.command(name = 'wfooter')
    @commands.has_permissions(manage_guild = True)
    async def wfooter_subcommands(self, ctx):

        prefix_1 = prefix_in_guild(self.bot, ctx.message)
        prefix = prefix_1[0]

        wfooter = discord.Embed(
            title=f'Информация про команду: {prefix}wfooter', 
            colour = discord.Color.teal(), 
            description=f'**Команда**: `[wfooter]`\n**Описание**: установить нижний текст приветствия\n**Использования**: `{prefix}wfooter [текст]`\n\n**Пример**: `{prefix}wfooter Удачки`'
        )
        wfooter.set_footer(
            text = ctx.message.author, 
            icon_url = ctx.message.author.avatar_url
        )
        wfooter.set_image(
            url = 'https://github.com/xzartsust/Tobi-Bot/blob/master/files/image/footer.png?raw=true'
        )
        await ctx.send(
            embed = wfooter
        ) 


    @help_for_commands.command(name = 'warn')
    @commands.has_permissions(manage_guild = True)
    async def warn_subcommands(self, ctx):

        prefix_1 = prefix_in_guild(self.bot, ctx.message)
        prefix = prefix_1[0]

        warn = discord.Embed(
            title=f'Информация про команду: {prefix}warn', 
            colour = discord.Color.teal(), 
            description=f'**Команда**: `[warn]`\n**Описание**: выдать предупреждение пользователю\n**Использования**: `{prefix}warn [пользователь]`\n\n**Пример**: `{prefix}warn @xZartsust#0000`'
        )
        warn.set_footer(
            text = ctx.message.author, 
            icon_url = ctx.message.author.avatar_url
        )
        await ctx.send(
            embed = warn
        ) 

    @help_for_commands.command(name = 'mwarn')
    @commands.has_permissions(manage_guild = True)
    async def mwarn_subcommands(self, ctx):

        prefix_1 = prefix_in_guild(self.bot, ctx.message)
        prefix = prefix_1[0]

        mwarn = discord.Embed(
            title=f'Информация про команду: {prefix}mwarn', 
            colour = discord.Color.teal(), 
            description=f'**Команда**: `[mwarn]`\n**Описание**: выдать предупреждение пользователю\n**Использования**: Просто `{prefix}mwarn` или `{prefix}mwarn @пользователь`\n\n**Пример**: `{prefix}mwarn` или `{prefix}mwarn @xZartsust#0000`'
        )
        mwarn.set_footer(
            text = ctx.message.author, 
            icon_url = ctx.message.author.avatar_url
        )
        await ctx.send(
            embed = mwarn
        ) 

    @help_for_commands.command(name = 'resetwarn')
    @commands.has_permissions(manage_guild = True)
    async def resetwarn_subcommands(self, ctx):

        prefix_1 = prefix_in_guild(self.bot, ctx.message)
        prefix = prefix_1[0]

        resetwarn = discord.Embed(
            title=f'Информация про команду: {prefix}resetwarn', 
            colour = discord.Color.teal(), 
            description=f'**Предостережение:** Эту команду можут использовать роли в которых есть права **Администратор и Управлять сервером**!\n**Команда**: `[resetwarn]`\n**Описание**: очистить все предупреждения\n**Использования**: `{prefix}resetwarn [пользователь]`\n\n**Пример**: `{prefix}resetwarn @xZartsust#0000`'
        )
        resetwarn.set_footer(
            text = ctx.message.author, 
            icon_url = ctx.message.author.avatar_url
        )
        await ctx.send(
            embed = resetwarn
        )
     
    @help_for_commands.command(name = 'send')
    async def send_subcommands(self, ctx):
        prefix_1 = prefix_in_guild(self.bot, ctx.message)
        prefix = prefix_1[0]

        send_emb=discord.Embed(
            timestamp= ctx.message.created_at, 
            title=f'Информация про команду: `{prefix}send`', 
            colour = discord.Color.teal(), 
            description=f'**Предостережение:** Эту команду можут использовать роли в которых есть права **Администратор**!\n**Команда**: `[send]`\n**Описание**: написать сообщения от имени бота\n**Использования**: `{prefix}send *text*`\n\n\n**Пример:** `{prefix}send Hello server`'
        )
        send_emb.set_footer(
            text = ctx.message.author,
            icon_url = ctx.message.author.avatar_url
        )
        await ctx.send(embed = send_emb)


    @help_for_commands.command(name = 'privatchnl')
    async def privatchnl_subcommands(self, ctx):
        prefix_1 = prefix_in_guild(self.bot, ctx.message)
        prefix = prefix_1[0]

        privatchnl_emb = discord.Embed(
            timestamp = ctx.message.created_at, 
            title = f'Информация про команду: `{prefix}privatchnl`', 
            colour = discord.Color.teal(), 
            description = f'**Предостережение:** Эту команду можут использовать роли в которых есть права **Администратор**!\n**Команда**: `[privatchnl]`\n**Описание**: задать канал и категорию для создания приватных голосовых каналов\n**Использования**: `{prefix}privatchnl *channel_id* *categori_id*`\n\n**Пример:** `{prefix}privatchnl 88416261844689851 181351848653489`'
        )
        privatchnl_emb.set_footer(
            text = ctx.message.author,
            icon_url = ctx.message.author.avatar_url
        )
        await ctx.send(embed = privatchnl_emb)

    @help_for_commands.command(name = 'resetprivchannel')
    async def resetprivchannel_subcommands(self, ctx):
        prefix_1 = prefix_in_guild(self.bot, ctx.message)
        prefix = prefix_1[0]

        resetprivchannel_emb=discord.Embed(
            timestamp= ctx.message.created_at, 
            title=f'Информация про команду: `{prefix}resetprivchannel`', 
            colour = discord.Color.teal(), 
            description=f'**Предостережение:** Эту команду можут использовать роли в которых есть права **Администратор**!\n**Команда**: `[resetprivchannel]`\n**Описание**: скинуть канал и категорию для создания приватных голосовых каналов\n**Использования**: `{prefix}resetprivchannel`\n\n**Пример:** `{prefix}privatchnl`'
        )
        resetprivchannel_emb.set_footer(
            text = ctx.message.author,
            icon_url = ctx.message.author.avatar_url
        )
        await ctx.send(embed = resetprivchannel_emb)


def setup(bot):
    bot.add_cog(HelpCommands(bot))
