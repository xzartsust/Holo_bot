import discord
from discord.ext import commands
import os
import asyncpg, asyncio
import psycopg2

####################################################################################################################

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


####################################################################################################################

def is_owner_guild(ctx):
    return ctx.author.id == ctx.guild.owner.id

class AuthoAddRole(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):

        cursor.execute(f'SELECT on_or_off FROM public."giveroles" WHERE guild_id = {member.guild.id};')
        on_or_off = cursor.fetchone()
        conn.commit()

        cursor.execute(f'SELECT role_id FROM public."giveroles" WHERE guild_id = {member.guild.id};')
        role = cursor.fetchone()
        conn.commit()

        role_1 = member.guild.get_role(role[0])

        if f'{on_or_off[0]}' == str('True'):
            await member.add_roles(role_1)
        elif f'{on_or_off[0]}' == str('False'):
            pass

    @commands.command()
    @commands.check(is_owner_guild)
    async def rwlc(self, ctx, role, types):
        guild = ctx.message.guild

        cursor.execute(f'UPDATE public."giveroles" SET role_id = \'{role}\' WHERE guild_id = \'{guild.id}\';')
        conn.commit()

        cursor.execute(f'UPDATE public."giveroles" SET on_or_off = \'{types}\' WHERE guild_id = \'{guild.id}\';')
        conn.commit()
        
        role1 = ctx.message.guild.get_role(role)
        print(role)

        emb = discord.Embed(
            title = 'Успешно!!!',
            description = f'Роль {role1} была установлена как автоматическая роль с функцией `{types}`',
            colour = discord.Color.green(),
            timestamp = ctx.message.created_at
        )

        if ctx.guild.system_channel is not None:
            await ctx.guild.system_channel.send(embed = emb)
        elif ctx.guild.system_channel is None:
            await ctx.send(embed = emb)
'''
    @rwlc.error
    async def welcome_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send('Третий аргумент может быть только true или false')
'''


def setup(bot):
    bot.add_cog(AuthoAddRole(bot))