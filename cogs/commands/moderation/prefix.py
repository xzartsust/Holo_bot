import discord
from discord.ext import commands
import os
import asyncpg, asyncio
import psycopg2

database = os.environ.get('DATABASE')
user = os.environ.get('USER')
password = os.environ.get('PASSWORD')
host = os.environ.get('HOST')
port = os.environ.get('PORT')

def is_owner_guild(ctx):
    return ctx.author.id == ctx.guild.owner.id

class prefix(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.command()
    @commands.check(is_owner_guild)
    async def prefix(self, ctx, prefix):

        

        guildid = ctx.guild.id
        try:
            conn = psycopg2.connect(
                database = f"{database}", 
                user = f"{user}", 
                password = f"{password}", 
                host = f"{host}", 
                port = "5432"
            )

            cursor = conn.cursor()
            
            cursor.execute(f'UPDATE public."myBD" SET prefix_guild=\'{prefix}\' WHERE guild_id = \'{guildid}\';')
            conn.commit()
            emb = discord.Embed(title = 'Выполнено успешно!', description = f'Префикс сервера изменений на "** {prefix} **"', colour = discord.Color.green(), timestamp = ctx.message.created_at)
            emb.set_footer(text = ctx.message.author)
            await ctx.send(embed = emb)

        except Exception as e:
            print(f'[{ctx.message.created_at}] [{ctx.message.guild.name}] [{ctx.message.guild.owner}] - [{e}]')
        
        finally:
            if(conn):
                cursor.close()
                conn.close()
                print("PostgreSQL connection is closed")
    
    async def cog_command_error(self, ctx: commands.Context, error: commands.CommandError):
        await ctx.send('Произошла ошибка: {}'.format(str(error)))
        print(f'[{ctx.message.created_at}] [{ctx.message.guild.name}] [{ctx.message.guild.owner}] - [{error}]')


def setup(bot):
    bot.add_cog(prefix(bot))
