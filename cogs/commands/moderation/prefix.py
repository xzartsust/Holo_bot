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

conn = psycopg2.connect(
    database = f"{database}", 
    user = f"{user}", 
    password = f"{password}", 
    host = f"{host}", 
    port = "5432"
)

cursor = conn.cursor()

def is_owner_guild(ctx):
    return ctx.author.id == ctx.guild.owner.id

class prefix(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.command()
    @commands.check(is_owner_guild)
    async def prefix(self, ctx, prefix):
        guildid = ctx.guild.id
        cursor.execute(f'UPDATE public."myBD" SET prefix_guild=\'{prefix}\' WHERE guild_id = \'{guildid}\';')
        conn.commit()
        emb = discord.Embed(title='Выполнено успешно!', description=f'Префикс сервера изменений на "** {prefix} **"', colour= discord.Color.green(), timestamp= ctx.message.created_at)
        emb.set_footer(text=ctx.message.author)
        await ctx.send(embed= emb)

    @prefix.error
    async def prefix_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            emb = discord.Embed(timestamp= ctx.message.created_at, title='Ошибка!!!', colour=discord.Color.red(), description='Эту команду может использовать только владелец сервера')
            emb.set_footer(text= ctx.message.author)
            await ctx.channel.purge(limit=1)
            await ctx.send(embed=emb)
def setup(bot):
    bot.add_cog(prefix(bot))
