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

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        join_guild_id = guild.id
        cursor.execute(f'INSERT INTO public."prefixDB" (guild_id, prefix) VALUES ({join_guild_id}, \'.\');')
        conn.commit()
    
    @commands.Cog.listener()
    async def on_guild_remove(self,guild):
        remove_guild_id = guild.id
        cursor.execute(f'DELETE FROM public."prefixDB" WHERE guild_id = {remove_guild_id};')
        conn.commit()
    
    @commands.command(aliases=['change_prefix','prefix'])
    @commands.check(is_owner_guild)
    async def change_prefix_server(self, ctx, prefix):
        guildid = ctx.guild.id
        cursor.execute(f'UPDATE public."prefixDB" SET prefix=\'{prefix}\' WHERE guild_id = \'{guildid}\';')
        conn.commit()
        emb = discord.Embed(title='Выполнено успешно!', description=f'Префикс сервера изменений на "***{prefix}***"', colour= discord.Color.green(), timestamp= ctx.message.created_at)
        await ctx.send(embed= emb)

def setup(bot):
    bot.add_cog(prefix(bot))
