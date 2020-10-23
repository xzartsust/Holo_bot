import discord
from discord.ext import commands
import os
import asyncio, asyncpg
import psycopg2

database = os.environ.get('DATABASE')
user = os.environ.get('USER')
password = os.environ.get('PASSWORD')
host = os.environ.get('HOST')
port = os.environ.get('PORT')

 
class PrefixServer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ['ps','sp'])
    async def prefixserver(self, ctx):
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

            cursor.execute(f'SELECT prefix_guild FROM public."myBD" WHERE guild_id = \'{guild.id}\';')
            prefix = cursor.fetchone()
        
        except (Exception, psycopg2.Error) as error:
            print ("Error while connecting to PostgreSQL", error)
        finally:
            if(conn):
                cursor.close()
                conn.close()
                print("PostgreSQL connection is closed")
        

        try:

            await ctx.send(f'Server Prefix: \"**{prefix[0]}**\"')
        
        except Exception as e:
            print(f'[{ctx.message.created_at}] [{ctx.message.guild.name}] [{ctx.message.guild.owner}] - [{e}]')
    
    async def cog_command_error(self, ctx: commands.Context, error: commands.CommandError):
        await ctx.send('Произошла ошибка: {}'.format(str(error)))
        print(f'[{ctx.message.created_at}] [{ctx.message.guild.name}] [{ctx.message.guild.owner}] - [{error}]')


def setup(bot):
    bot.add_cog(PrefixServer(bot))

