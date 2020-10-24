import discord
from discord.ext import commands
import psycopg2
import os
import asyncpg

database = os.environ.get('DATABASE')
user = os.environ.get('USER')
password = os.environ.get('PASSWORD')
host = os.environ.get('HOST')
port = os.environ.get('PORT')


class ResetWarns(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator = True)
    async def resetwarn(self, ctx, member: discord.Member):
        guild = ctx.message.guild
        member_id = member.id
        
        try:
            conn = psycopg2.connect(
                database = f"{database}", 
                user = f"{user}", 
                password = f"{password}", 
                host = f"{host}", 
                port = "5432"
            )
            cursor = conn.cursor()

            cursor.execute(f'SELECT member_id FROM public."Warns" WHERE guild_id = \'{guild.id}\' AND member_id = \'{member_id}\';')
            memberDB = cursor.fetchone()
            conn.commit()
            
            cursor.execute(f'SELECT guild_id FROM public."Warns" WHERE guild_id = \'{guild.id}\' AND member_id = \'{member_id}\';')
            guildDB = cursor.fetchone()
            conn.commit()

            cursor.execute(f'SELECT counts FROM public."Warns" WHERE guild_id = \'{guild.id}\' AND member_id = \'{member_id}\';')
            counts = cursor.fetchone()
            conn.commit()
        
        except (Exception, psycopg2.Error) as error:
            print ("Error while connecting to PostgreSQL", error)
        finally:
            if(conn):
                cursor.close()
                conn.close()
                print("PostgreSQL connection is closed")
        
        try:
            

            if memberDB is None and guildDB is None:
                
                await ctx.send('У этого пользователя не предупреждений')
            
            elif counts[0] == '0':

                await ctx.send('У этого пользователя не предупреждений')
            
            else:

                cursor.execute(f'UPDATE public."Warns" SET counts = \'0\' WHERE guild_id= \'{guild.id}\' AND member_id = \'{member_id}\';')
                conn.commit()

        except Exception as e:
            print(f'[{ctx.message.created_at}] [{ctx.message.guild.name}] [{ctx.message.guild.owner}] - [{e}]')
        
    
    async def cog_command_error(self, ctx: commands.Context, error: commands.CommandError):
        await ctx.send('Произошла ошибка: {}'.format(str(error)))
        print(f'[{ctx.message.created_at}] [{ctx.message.guild.name}] [{ctx.message.guild.owner}] - [{error}]')


def setup(bot):
    bot.add_cog(ResetWarns(bot))