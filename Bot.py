# This Python file uses the following encoding: utf-8
import discord
from discord import utils
from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import get
from config_for_bot import *
import youtube_dl
import os
import datetime
import logging
import time
import asyncio
from itertools import cycle
from Cybernator import Paginator as pag

########################################################## Вивод логів ###################################################


logger= logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler= logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s: %(message)s'))
logger.addHandler(handler)


########################################################################################################################


bot=commands.Bot(command_prefix='.')
bot.remove_command('help')


############################################################# Події бота #################################################


async def change_status():
    await bot.wait_until_ready()
    msg= cycle(status)

    while not bot.is_closed():
        next_status= next(msg)
        await bot.change_presence(activity= discord.Game(name=next_status))
        await asyncio.sleep(15)


@bot.event #включення бота
async def on_ready():
    print('Connect')



@bot.event #Відповіть на затрігерені слова
async def on_message(message):
    await bot.process_commands(message)
    authotm = message.author.mention
    msg= message.content.lower()
    if msg in greetings:
        await message.channel.send(f'{authotm} '+'Hello')
    if msg in goodbye:
        await message.channel.send(f'{authotm} '+'Goodbye and sweet dream')
    if msg in help_for_server:
        await message.channel.send(f'{authotm} '+'Write .help and you get commands this server')

    if message.content.startswith('.hello'):
        await message.channel.send('Hello {0.author.mention}'.format(message))



######################################################### Команди бота ###################################################


@bot.command(pass_context= True)
async def user(ctx, member: discord.Member):


    time_to_join_in_discord = member.created_at
    time_to_join_in_server = member.joined_at
    now = datetime.datetime.now()
    delta_s = now - time_to_join_in_server
    delta_d= now - time_to_join_in_discord
    b= delta_d.days
    a = delta_s.days


    if member.bot is False and member.nick is not None:
        emb = discord.Embed(title=format(member), colour=discord.Color.green(), url=f'{member.avatar_url}',inline=False)
        emb.add_field(name='Присоединился к Discord',value=f'{time_to_join_in_discord.strftime("%d.%m.%Y %H:%M")}\n ({b} дней)',inline=False)
        emb.add_field(name='Присоединился к серверу',value=f'{time_to_join_in_server.strftime("%d.%m.%Y %H:%M")}\n ({a} дней)',inline=False)
        emb.add_field(name='Самая высокая роль', value=str(member.top_role.mention), inline=False)
        emb.add_field(name='Айди', value=member.id, inline=False)

        if member.status == discord.Status.online:
            emb.add_field(name='Status', value='Онлайн', inline=False)
        elif member.status == discord.Status.dnd:
            emb.add_field(name='Status', value='Не беспокоить', inline=False)
        elif member.status == discord.Status.offline:
            emb.add_field(name='Status', value='Нет в сети', inline=False)
        elif member.status == discord.Status.idle:
            emb.add_field(name='Status', value='Отошол', inline=False)

        if member.activity is not None:
            emb.add_field(name='Кастом статус', value=member.activity, inline=False)
        else:
            emb.add_field(name='Кастом статус', value='Нету', inline=False)

        emb.set_thumbnail(url=member.avatar_url)
        emb.set_author(name=member.nick)
        emb.set_footer(text='Заптрос от: ' + f'{ctx.author}' + f' Сегодня об: {now.strftime("%H:%M")}')

        await ctx.channel.purge(limit=1)
        await ctx.send(embed=emb)

    if member.bot is False and member.nick is None:
        emb = discord.Embed(title=format(member), colour=discord.Color.green(), url=f'{member.avatar_url}',
                            inline=False)
        emb.add_field(name='Присоединился к Discord',
                      value=f'{time_to_join_in_discord.strftime("%d.%m.%Y %H:%M")}\n ({b} дней)', inline=False)
        emb.add_field(name='Присоединился к серверу',
                      value=f'{time_to_join_in_server.strftime("%d.%m.%Y %H:%M")}\n ({a} дней)', inline=False)
        emb.add_field(name='Самая высокая роль', value=str(member.top_role.mention), inline=False)
        emb.add_field(name='Айди', value=member.id, inline=False)

        if member.status == discord.Status.online:
            emb.add_field(name='Status', value='Онлайн', inline=False)
        elif member.status == discord.Status.dnd:
            emb.add_field(name='Status', value='Не беспокоить', inline=False)
        elif member.status == discord.Status.offline:
            emb.add_field(name='Status', value='Нет в сети', inline=False)
        elif member.status == discord.Status.idle:
            emb.add_field(name='Status', value='Отошол', inline=False)

        if member.activity is not None:
            emb.add_field(name='Кастом статус', value= member.activity,inline=False)
        else:
            emb.add_field(name='Кастом статус', value='Нету', inline=False)

        emb.set_thumbnail(url=member.avatar_url)
        emb.set_footer(text='Заптрос от: ' + f'{ctx.author}' + f' Сегодня об: {now.strftime("%H:%M")}')

        await ctx.channel.purge(limit=1)
        await ctx.send(embed=emb)

    if member.bot is True and member.nick is None:
        emb = discord.Embed(title=format(member), colour=discord.Color.green(), url=f'{member.avatar_url}',
                            inline=False)
        emb.add_field(name='Присоединился к Discord',
                      value=f'{time_to_join_in_discord.strftime("%d.%m.%Y %H:%M")}\n ({b} дней)', inline=False)
        emb.add_field(name='Присоединился к серверу',
                      value=f'{time_to_join_in_server.strftime("%d.%m.%Y %H:%M")}\n ({a} дней)', inline=False)
        emb.add_field(name='Самая высокая роль', value=str(member.top_role.mention), inline=False)
        emb.add_field(name='Айди', value=member.id, inline=False)

        if member.status == discord.Status.online:
            emb.add_field(name='Status', value='Онлайн', inline=False)
        elif member.status == discord.Status.dnd:
            emb.add_field(name='Status', value='Не беспокоить', inline=False)
        elif member.status == discord.Status.offline:
            emb.add_field(name='Status', value='Нет в сети', inline=False)
        elif member.status == discord.Status.idle:
            emb.add_field(name='Status', value='Отошол', inline=False)

        emb.add_field(name='Кастомный статус', value=f'Кастомный статус: {member.activity}')

        emb.set_thumbnail(url=member.avatar_url)
        emb.set_footer(text='Заптрос от: ' + f'{ctx.author}' + f' Сегодня об: {now.strftime("%H:%M")}')

        await ctx.channel.purge(limit=1)
        await ctx.send(embed=emb)

    if member.bot is True and member.nick is not None:
        emb = discord.Embed(title=format(member), colour=discord.Color.green(), url=f'{member.avatar_url}',
                            inline=False)
        emb.add_field(name='Присоединился к Discord',
                      value=f'{time_to_join_in_discord.strftime("%d.%m.%Y %H:%M")}\n ({b} дней)', inline=False)
        emb.add_field(name='Присоединился к серверу',
                      value=f'{time_to_join_in_server.strftime("%d.%m.%Y %H:%M")}\n ({a} дней)', inline=False)
        emb.add_field(name='Самая высокая роль', value=str(member.top_role.mention), inline=False)
        emb.add_field(name='Айди', value=member.id, inline=False)

        if member.status == discord.Status.online:
            emb.add_field(name='Status', value='Онлайн', inline=False)
        elif member.status == discord.Status.dnd:
            emb.add_field(name='Status', value='Не беспокоить', inline=False)
        elif member.status == discord.Status.offline:
            emb.add_field(name='Status', value='Нет в сети', inline=False)
        elif member.status == discord.Status.idle:
            emb.add_field(name='Status', value='Отошол', inline=False)

        emb.add_field(name='Кастомный статус',value=f'Кастомный статус: {member.activity}', inline=False)

        emb.set_thumbnail(url=member.avatar_url)
        emb.set_author(name=member.nick)
        emb.set_footer(text='Заптрос от: ' + f'{ctx.author}' + f' Сегодня об: {now.strftime("%H:%M")}')

        await ctx.channel.purge(limit=1)
        await ctx.send(embed=emb)


@bot.command()
@commands.has_permissions(administrator= True)
async def logout(ctx):
    await bot.logout()


@bot.command()
async def bot_servers(ctx):
    emb=discord.Embed(description=f'Присутствует на {str(len(bot.guilds))} серверах', colour=discord.Color.blurple())
    await ctx.send(embed= emb)



@bot.command(aliases=['info','i'])#команда .help
async def help(ctx):
    await ctx.channel.purge(limit=1)
    now = datetime.datetime.now()

    emb= discord.Embed(title='Помощ по использованию бота', description='Здесь вы можете узнать про осноные команды бота')

    emb1= discord.Embed(title='Команды бота')
    emb1.add_field(name='`{}user @имя`'.format(PREFIX),value=' - Информация про пользователя', inline=False)
    emb1.add_field(name='`{}help` или `{}info` или `{}i`'.format(PREFIX,PREFIX,PREFIX),value=' - Команды бота', inline=False)
    emb1.add_field(name='`{}ping`'.format(PREFIX),value=' - Посмотреть пинг бота', inline=False)
    emb1.add_field(name='`{}bot_servers`'.format(PREFIX),value=' - Посмотреть на скольких серверах есть етот бот', inline=False)

    emb2=discord.Embed(title='Команды для модерации')
    emb2.add_field(name='`{}ban @имя причина`'.format(PREFIX),value=' - Выдать бан игрок', inline=False)
    emb2.add_field(name='`{}mute @имя`'.format(PREFIX),value=' - Замутить игрока', inline=False)
    emb2.add_field(name='`{}unban @имя`'.format(PREFIX),value='- Розбанить играка на етом сервере', inline=False)
    emb2.add_field(name='`{}kick @имя причина`'.format(PREFIX),value='- Вигнать игрока с етого сервера', inline=False)
    emb2.add_field(name='`{}clear`'.format(PREFIX),value='- Очыстка чата', inline=False)

    embeds=[emb,emb1,emb2]
    message= await ctx.send(embed= emb1)
    page= pag(bot, message, only=ctx.author, use_more=False, embeds=embeds, color=0x008000)

    await page.start()

@bot.command(pass_context= True)
async def helpmoder(ctx):
    await ctx.channel.purge(limit=1)
    now = datetime.datetime.now()

    emb= discord.Embed(title='Команди бота', colour= discord.Color.green())
    emb.add_field(name='`{}ban @имя причина`'.format(PREFIX), value='Выдать бан игроку', inline=False)
    emb.add_field(name='`{}mute @имя`'.format(PREFIX), value='Замутить игрока', inline=False)
    emb.add_field(name='`{}unban @имя`'.format(PREFIX), value='Розбанить играка на етом сервере', inline=False)
    emb.add_field(name='`{}kick @имя причина`'.format(PREFIX), value='Вигнать игрока с етого сервера',inline=False)
    emb.add_field(name='`{}clear`'.format(PREFIX), value='Очыстка чата', inline=False)
    emb.set_footer(text='Заптрос от: ' + f'{ctx.author}' + f' Сегодня об: {now.strftime("%H:%M")}')

    await ctx.send(embed= emb)



@bot.command()#пінг бота
async def ping(ctx):
    time_1 = time.perf_counter()
    await ctx.trigger_typing()
    time_2 = time.perf_counter()
    ping = round((time_2 - time_1) * 1000)
    emb= discord.Embed(description=f'Ping: {ping}ms',colour=discord.Color.blurple())
    await ctx.send(embed= emb)


@bot.command()
@commands.has_permissions(administrator=True, manage_messages=True,manage_guild=True,view_audit_log=True, mention_everyone=True)
async def clear(ctx, arg):
    await ctx.channel.purge(limit= int(arg))


@bot.command()
async def tuser(ctx):
    all_users = set([])
    for user in bot.get_all_members():
        all_users.add(user) # will not add the same user twice since it's a set type.
    await ctx.send('Total users in all my servers combined: ' + str(len(all_users)))

'''
@bot.command(pass_context= True)#приєднаня бота до голосового каналу
@commands.has_permissions(administrator= True)
async def join(ctx):
     global voice
     channel = ctx.message.author.voice.channel
     voice = get(bot.voice_clients, guild= ctx.guild)

     emb = discord.Embed(description=f'Бот подключился к каналу: {channel}', color=0x008000)

     if voice and voice.is_connected():
         await voice.move_to(channel)
     else:
         voice = await channel.connect()
         await ctx.send(embed=emb)


@bot.command(pass_context= True)#виход бота з голосового
@commands.has_permissions(administrator= True)
async def leave(ctx):
     global voice
     channel = ctx.message.author.voice.channel
     voice = get(bot.voice_clients, guild= ctx.guild)

     await ctx.channel.purge(limit=1)

     emb = discord.Embed(description=f'Бот отключился от каналу: {channel}', color=discord.Color.red())

     if voice and voice.is_connected():
         await voice.disconnect()
         await ctx.send(embed=emb)
     else:
         voice = await channel.disconnect()


@bot.command()#музика разом з приєднаням до голосового чату
@commands.has_permissions(administrator= True)
async def play(ctx, url: str):
     global voice
     channel = ctx.message.author.voice.channel
     voice = get(bot.voice_clients, guild=ctx.guild)

     emb3= discord.Embed(title=f'Бот підключився до: {channel}', colour=discord.Color.green())

     if voice and voice.is_connected():
         await voice.move_to(channel)
     else:
         voice = await channel.connect()
         await ctx.send(embed= emb3)
         print(f'bot is connected to: {channel}')

     song_there= os.path.isfile('song.mp3')

     try:
         if song_there:
             os.remove('song.mp3')
             print('[Log] Старий файл видалено')
     except PermissionError:
         print('[Log] Невдалося удалити файл')

     emb= discord.Embed(title='Загрузка музики...', colour=0xFFFF00)
     await ctx.send(embed= emb)

     voice = get(bot.voice_clients, guild=ctx.guild)

     with youtube_dl.YoutubeDL(ydl_options) as ydl:
         print('[Log] Загружаю...')
         ydl.download([url])
     for file in os.listdir('./'):
         if file.endswith('.mp3'):
             name = file
             print(f'[Log] Перейменовую файл: {file}')
             os.rename(file, 'song.mp3')


     emb2= discord.Embed(title=f'{name} музика закінчилася', colour=discord.Color.green())

     voice.play(discord.FFmpegPCMAudio('song.mp3'), after= lambda e: ctx.send(embed= emb2))
     voice.source= discord.PCMVolumeTransformer(voice.source)
     voice.source.volume= 0.1
     song_name=name.rsplit('-', 2)

     emb1= discord.Embed(title=f'Зараз гарє музика {song_name[0]}', colour=discord.Color.dark_gold())
     await ctx.send(embed= emb1)
'''
@bot.command(pass_context= True)#команда кік
@commands.has_permissions(administrator=True, kick_members=True, ban_members=True,manage_guild=True,view_audit_log=True, mention_everyone=True)
async def kick(ctx, member: discord.Member, *, reason):
    await ctx.channel.purge(limit=1)
    await member.kick(reason= reason)
    await ctx.send(f'Юзер {member.mention} був вигнаний з сервера по причині {reason}')

@bot.command(pass_context= True)#команда бан
@commands.has_permissions(administrator=True,ban_members=True,kick_members=True,manage_guild=True,view_audit_log=True, mention_everyone=True)
async def ban(ctx, guild: discord.Guild, *,arg, member: discord.Member):
    await ctx.channel.purge(limit=1)
    await guild.ban(user= member.mention,delete_message_days= 1,reason= arg)
    await ctx.send(f'Юзер {member.mention} був забанений на цьому сервері')


@bot.command(pass_context= True)#команда яка снімає бан
@commands.has_permissions(administrator=True, ban_members=True,kick_members=True,manage_guild=True,view_audit_log=True, mention_everyone=True)
async def unban(ctx, *, member):
    await ctx.channel.purge(limit=1)
    ban_users= await ctx.guild.bans()
    for ban_entry in ban_users:
        user= ban_entry.user
        await ctx.guild.unban(user)
        await ctx.send(f'Юзер {user.mention} розбанений')
        return

@bot.command(pass_context= True)#список забанених юзерів покишо тільки в консоль, зробити шоб виводилося в ембед
async def banlist(ctx, user: discord.User):
    await ctx.channel.purge(limit=1)
    ban_list= await ctx.guild.bans()
    print(ban_list)


@bot.command()
@commands.has_permissions(ban_members=True)
@commands.has_permissions(administrator=True, kick_members=True,manage_guild=True,view_audit_log=True, mention_everyone=True)
async def mute(ctx, member: discord.Member):
    await ctx.channel.purge(limit=1)
    mute_rol= discord.utils.get(ctx.message.guild.roles, name= 'MUTE')
    await member.add_roles(mute_rol)
    await ctx.send(f'{member.mention} MUTE!')

####################################################### Робота з помилками ###############################################

@clear.error
async def clear_error(ctx,error):
    if isinstance(error, commands.MissingPermissions):
        emb = discord.Embed(title='Ошибка!!!', colour=discord.Color.red(),description='У вас нет прав на ету команду')
        await ctx.channel.purge(limit=1)
        await ctx.send(embed=emb)

@mute.error
async def mute_error(ctx,error):
    if isinstance(error, commands.MissingPermissions):
        emb = discord.Embed(title='Ошибка!!!', colour=discord.Color.red(),description='У вас нет прав на ету команду')
        await ctx.channel.purge(limit=1)
        await ctx.send(embed=emb)

@banlist.error
async def banlist_error(ctx,error):
    if isinstance(error, commands.MissingPermissions):
        emb = discord.Embed(title='Ошибка!!!', colour=discord.Color.red())
        emb.add_field(name='Ошибка в доступі до команди', value='Нажаль ви не маєте права застосувати цю команду')
        await ctx.channel.purge(limit=1)
        await ctx.send(embed=emb)

@unban.error
async def unban_error(ctx,error):
    if isinstance(error, commands.MissingPermissions):
        emb = discord.Embed(title='Ошибка!!!', colour=discord.Color.red())
        emb.add_field(name='Ошибка в доступі до команди', value='Нажаль ви не маєте права застосувати цю команду')
        await ctx.channel.purge(limit=1)
        await ctx.send(embed=emb)

@ban.error
async def ban_error(ctx,error):
    if isinstance(error, commands.MissingPermissions):
         emb = discord.Embed(title='Ошибка!!!', colour=discord.Color.red(),description='У вас нет прав на ету команду')
         await ctx.channel.purge(limit=1)
         await ctx.send(embed=emb)

@kick.error
async def kick_error(ctx,error):
    if isinstance(error, commands.MissingPermissions):
        emb = discord.Embed(title='Ошибка!!!', colour=discord.Color.red(),description='У вас нет прав на ету команду')
        await ctx.channel.purge(limit=1)
        await ctx.send(embed=emb)


@user.error
async def user_error(ctx,error):
    if isinstance(error, commands.MissingRequiredArgument):
        emb= discord.Embed(title='Ошибка', colour=discord.Color.red(), description='Пожалуйста укажите игрока о котором хотите узнать информацию')
        await ctx.channel.purge(limit=1)
        await ctx.send(embed= emb)

@helpmoder.error
async def helpmoser_error(ctx, error):
    if isinstance(error, commands.MissingAnyRole):
        emb = discord.Embed(title='Ошибка', colour=discord.Color.red(),description='У вас нет прав на ету команду')
        await ctx.channel.purge(limit=1)
        await ctx.send(embed=emb)








TOKEN = os.environ.get('TOKEN')

bot.loop.create_task(change_status())
bot.run('TOKEN')
