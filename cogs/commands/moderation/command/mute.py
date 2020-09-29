import discord
from discord.ext import commands
import psycopg2
import asyncio, asyncpg
import os

########################################################## Connect to SQL ###################################################


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


########################################################################################################################

class MuteCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members = True)
    async def mute(self, ctx, who: discord.Member, reason: str = None):
        
        guild = ctx.message.guild
        try:
            
            cursor.execute(f'SELECT role_for_mute FROM public."myBD" WHERE guild_id = \'{guild.id}\';')
            role_mute = cursor.fetchone()
            conn.commit()
            
            role = ctx.message.guild.get_role(role_mute[0])
            await ctx.channel.purge(limit = 1)
        
            if reason is None:
                
                mute = discord.Embed(
                    title = f'{who} получил мут',
                    timestamp = ctx.message.created_at,
                    colour = discord.Color.green()
                    ) 
                mute.add_field(
                    name = 'Пользователь',
                    value = f'{who.mention}'
                    )
                mute.add_field(
                    name = 'Модератор',
                    value = f'{ctx.message.author.mention}'
                    )
                mute.add_field(
                    name = 'Причина',
                    value = 'Не указана'
                )
                
                await ctx.send(embed = mute)
                await who.add_roles(role)
            
            else:
                
                mute = discord.Embed(
                    title = f'{who} получил мут',
                    timestamp = ctx.message.created_at,
                    colour = discord.Color.green()
                    ) 
                mute.add_field(
                    name = 'Пользователь',
                    value = f'{who.mention}'
                    )
                mute.add_field(
                    name = 'Модератор',
                    value = f'{ctx.message.author.mention}'
                    )
                mute.add_field(
                    name = 'Причина',
                    value = f'{reason}'
                )
                
                await ctx.send(embed = mute)
                await who.add_roles(role)
        
        except AttributeError:
            pass
        
        except Exception as e:
            print(f'[{ctx.message.created_at}] [{ctx.message.guild.name}] [{ctx.message.guild.owner}] - [{e}]')
    
    async def cog_command_error(self, ctx: commands.Context, error: commands.CommandError):
        await ctx.send('Произошла ошибка: {}'.format(str(error)))
        print(f'[{ctx.message.created_at}] [{ctx.message.guild.name}] [{ctx.message.guild.owner}] - [{error}]')
        

        '''
        if what == str('m'):
            if time >=1 and time <= 59:
                
                await ctx.send(f'--> {who} получил мут на {time}м. по причине: {reason}')

                await who.add_roles(role)
                await who.move_to(None)
                await asyncio.sleep(time * 60)
                await who.remove_roles(role)
                await ctx.send('Мут забраний')
        
        if what == str('h'):
            if time >= 1 and time <= 24:
                await ctx.send(f'--> {who} получил мут на {time}ч. по причине: {reason}')

                await who.add_roles(role)
                await who.move_to(None)
                await asyncio.sleep(time * 3600)
                await who.remove_roles(role)
                await ctx.send('Мут забраний')
        
        if what == str('d'):
            if time >= 1 and time <= 365:
                await ctx.send(f'--> {who} получил мут на {time}д. по причине: {reason}')

                await who.add_roles(role)
                await who.move_to(None)
                await asyncio.sleep(time * 86400)
                await who.remove_roles(role)
                await ctx.send('Мут забраний')
        
        if what == str('y'):
            if time >= 1:
                await ctx.send(f'--> {who} получил мут на {time}л. по причине: {reason}')

                await who.add_roles(role)
                await who.move_to(None)
                await asyncio.sleep(time * 31557600)
                await who.remove_roles(role)
                await ctx.send('Мут забраний') 
        '''

def setup(bot):
    bot.add_cog(MuteCommand(bot))