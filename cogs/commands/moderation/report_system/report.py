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

class ReportUser(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 21600, commands.BucketType.member)
    async def report(self, ctx, member: discord.Member = None, *, reason: str = None):
        
        guild = ctx.message.guild
        user = ctx.message.author
        try:
            conn = psycopg2.connect(
                database = f"{database}", 
                user = f"{user}", 
                password = f"{password}", 
                host = f"{host}", 
                port = "5432"
            )

            cursor = conn.cursor()

            cursor.execute(f'SELECT report_channel FROM public."myBD" WHERE guild_id = {guild.id};')
            chanel = cursor.fetchone()
            conn.commit()

            if chanel[0] is None:
                await ctx.send('Ошибка! У вас не указан канал для репортов. Установить канал вы можете с помощю команди reportchannel', delete_after = 10)
            if reason is None:
                await ctx.send('Укажите, пожалуста, причину репорта!', delete_after = 5)
            elif member is None:
                await ctx.send('Укажите, пожалуйста, пользователя на которого вы хотите пожаловаться!', delete_after = 5)
            else:
                channel = self.bot.get_channel(chanel[0])
                await channel.send(f'Пользователь {member.mention} получил жадолобу от {user.mention} по причине: {reason}')
            

        except Exception as e:
            print(f'[{ctx.message.created_at}] [{ctx.message.guild.name}] [{ctx.message.guild.owner}] - [{e}]')

        finally:
            if(conn):
                cursor.close()
                conn.close()

def setup(bot):
    bot.add_cog(ReportUser(bot))