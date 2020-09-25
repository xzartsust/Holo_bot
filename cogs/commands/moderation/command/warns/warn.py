import discord
from discord.ext import commands
import asyncpg
import psycopg2
import os

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

class Warns(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def warn(self, ctx, member: discord.Member):

        guild = ctx.message.guild
        member_id = member.id

        try:
            
            cursor.execute(f'SELECT member_id FROM public."Warns" WHERE guild_id = \'{guild.id}\' AND member_id = \'{member_id}\';')
            memberDB = cursor.fetchone()
            conn.commit()
            
            cursor.execute(f'SELECT guild_id FROM public."Warns" WHERE guild_id = \'{guild.id}\' AND member_id = \'{member_id}\';')
            guildDB = cursor.fetchone()
            conn.commit()
            
            if memberDB is None and guildDB is None:
                
                cursor.execute(f'INSERT INTO public."Warns" (guild_id, member_id) VALUES (\'{guild.id}\',\'{member_id}\');')
                conn.commit()

                cursor.execute(f'SELECT counts FROM public."Warns" WHERE guild_id = \'{guild.id}\' AND member_id = \'{member_id}\';')
                count = cursor.fetchone()
                conn.commit()
                
                count_now = count[0] + 1
            
                cursor.execute(f'UPDATE public."Warns" SET counts = \'{count_now}\' WHERE guild_id= \'{guild.id}\' AND member_id = \'{member_id}\';')
                conn.commit()
            
            else:
            
                cursor.execute(f'SELECT counts FROM public."Warns" WHERE guild_id = \'{guild.id}\' AND member_id = \'{member_id}\';')
                count = cursor.fetchone()
                conn.commit()
            
                count_now = count[0] + 1
            
                cursor.execute(f'UPDATE public."Warns" SET counts = \'{count_now}\' WHERE guild_id= \'{guild.id}\' AND member_id = \'{member_id}\';')
                conn.commit()
        
        except Exception as e:
            print(e)

def setup(bot):
    bot.add_cog(Warns(bot))