import discord
from discord.ext import commands
import asyncpg, asyncio
import psycopg2
import os
from discord import utils
from discord.utils import get

database = os.environ.get('DATABASE')
user = os.environ.get('USER')
password = os.environ.get('PASSWORD')
host = os.environ.get('HOST')
port = os.environ.get('PORT')


def is_owner_guild(ctx):
    return ctx.author.id == ctx.guild.owner.id

class member_greeting(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        
        

        description_defolt = 'Каждый участник этого сервере равен перед другими. Поэтому настоятельно просим ознакомиться с правилами сервера\nЗаранее благодарим Вас за вежливость и адекватность.'

        try:
            conn = psycopg2.connect(
                database = f"{database}", 
                user = f"{user}", 
                password = f"{password}", 
                host = f"{host}", 
                port = "5432"
            )

            cursor = conn.cursor()
            
            cursor.execute(f'SELECT welcome_channel FROM public."myBD" WHERE guild_id = \'{member.guild.id}\';')
            chan = cursor.fetchone()
            conn.commit()
            
            cursor.execute(f'SELECT wlc_chan_t_or_f FROM public."myBD" WHERE guild_id = \'{member.guild.id}\';')
            yes_or_not = cursor.fetchone()
            conn.commit()

            cursor.execute(f'SELECT title FROM public."Texts_For_Welcome" WHERE guild_id = \'{member.guild.id}\';')
            title = cursor.fetchone()
            conn.commit()

            cursor.execute(f'SELECT description FROM public."Texts_For_Welcome" WHERE guild_id = \'{member.guild.id}\';')
            description = cursor.fetchone()
            conn.commit()

            cursor.execute(f'SELECT footer FROM public."Texts_For_Welcome" WHERE guild_id = \'{member.guild.id}\';')
            footer = cursor.fetchone()
            conn.commit()
            
            channel = self.bot.get_channel(chan[0])
            
            if f'{yes_or_not[0]}' == str('True'):
                if description[0] is None or title[0] is None or footer[0] is None:#написати в описі до команди що обовязково має бути вказані title і description  якщо цього не буде вказано
                    #, або буде вказано тільки щось одне з них то буде спрацьовувати дефолтне привітння9вказати яке)
                    emb = discord.Embed(
                        title = f'Приветствуем Вас на {member.guild.name}!',
                        description = f'{description_defolt}',
                        colour = discord.Color.green()
                    )
                    emb.set_thumbnail(
                        url = member.avatar_url
                    )
                    emb.set_footer(
                        text = f'{member.id}' + ' | Приятного времяпрепровождения!',
                        icon_url= 'https://github.com/xzartsust/holo_bot/blob/master/files/image/id.png?raw=true'
                    )
                    await channel.send(f'{member.mention}', embed = emb)
                else:
                    emb = discord.Embed(
                        title = f'{title[0]} {member.guild.name}!',
                        description = f'{description[0]}',
                        colour = discord.Color.green()
                    )
                    emb.set_thumbnail(
                        url = member.avatar_url
                    )
                    emb.set_footer(
                        text = f'{member.id}' + f' | {footer[0]}',
                        icon_url= 'https://github.com/xzartsust/holo_bot/blob/master/files/image/id.png?raw=true'
                    )
                    await channel.send(f'{member.mention}', embed = emb)
            
            if f'{yes_or_not[0]}' == str('False'):
                pass
        
        except Exception as e:
            print(f'[{e}]')
        
        finally:
            if(conn):
                cursor.close()
                conn.close()
                

    @commands.command(aliases=['wlc'])
    @commands.has_permissions(administrator = True)
    async def welcome(self, ctx, channel: int, types: bool):

        

        guild = ctx.message.guild
        
        try:
            conn = psycopg2.connect(
                database = f"{database}", 
                user = f"{user}", 
                password = f"{password}", 
                host = f"{host}", 
                port = "5432"
            )

            cursor = conn.cursor()
            cursor.execute(f'UPDATE public."myBD" SET welcome_channel = \'{channel}\', wlc_chan_t_or_f = \'{types}\' WHERE guild_id = \'{guild.id}\';')
            conn.commit()
            
            channel1 = ctx.message.guild.get_channel(channel)
            
            emb = discord.Embed(
                title = 'Успешно!!!',
                description = f'Канал уведомлений "Welcome" был установлен на `{channel1}` с функцией `{types}`',
                colour = discord.Color.green(),
                timestamp = ctx.message.created_at
            )
            
            if ctx.guild.system_channel is not None:
                await ctx.guild.system_channel.send(embed = emb)
            elif ctx.guild.system_channel is None:
                await ctx.send(embed = emb)

        except Exception as e:
            print(f'[{ctx.message.created_at}] [{ctx.message.guild.name}] [{ctx.message.guild.owner}] - [{e}]')
        
        finally:
            if(conn):
                cursor.close()
                conn.close()
                
    
    async def cog_command_error(self, ctx: commands.Context, error: commands.CommandError):
        await ctx.send('Произошла ошибка: {}'.format(str(error)))
        print(f'[{ctx.message.created_at}] [{ctx.message.guild.name}] [{ctx.message.guild.owner}] - [{error}]')



def setup(bot):
    bot.add_cog(member_greeting(bot))