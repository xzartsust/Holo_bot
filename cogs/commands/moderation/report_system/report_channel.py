import discord
from discord.ext import commands
from discord.utils import get
import asyncpg
import psycopg2
import os

database = os.environ.get('DATABASE')
user = os.environ.get('USER')
password = os.environ.get('PASSWORD')
host = os.environ.get('HOST')
port = os.environ.get('PORT')

class ReportChannel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator = True)
    async def reportchannel(self, ctx, channel = None):
        
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
            
            if isinstance(channel, int) is True:
                cursor.execute(f'UPDATE public."myBD" SET report_channel = \'{channel}\' WHERE guild_id = \'{guild.id}\';')
                conn.commit()
                canal = self.bot.get_channel(channel)
                await ctx.send(f'Канала {canal.mention} был установлен для *Репортов*')
            elif channel is None:
                await ctx.send('Ошибка! Укажите айди канала!', delete_after = 5)
            elif isinstance(channel, int) is False:
                await ctx.send('Ошибка! Вы можете указать только айди канала!', delete_after = 5)
        
        
        except Exception as e:
            print(f'[{ctx.message.created_at}] [{ctx.message.guild.name}] [{ctx.message.guild.owner}] - [{e}]')
        
        finally:
            if (conn):
                cursor.close()
                conn.close()

def setup(bot):
    bot.add_cog(ReportChannel(bot))

