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

class AuthoAddRole(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):

        

        try:
            conn = psycopg2.connect(
                database = f"{database}", 
                user = f"{user}", 
                password = f"{password}", 
                host = f"{host}", 
                port = "5432"
            )

            cursor = conn.cursor()

            cursor.execute(f'SELECT wlc_role_t_or_f FROM public."myBD" WHERE guild_id = {member.guild.id};')
            on_or_off = cursor.fetchone()
            conn.commit()

            cursor.execute(f'SELECT wlc_role FROM public."myBD" WHERE guild_id = {member.guild.id};')
            role = cursor.fetchone()
            conn.commit()

            role_1 = member.guild.get_role(role[0])

            if f'{on_or_off[0]}' == str('True'):
                await member.add_roles(role_1)
            elif f'{on_or_off[0]}' == str('False'):
                pass

        except Exception as e:
            print(f'[{e}]')
        
        finally:
            if(conn):
                cursor.close()
                conn.close()
                
    
    @commands.command()
    @commands.check(is_owner_guild)
    async def rwlc(self, ctx, role: int, types: bool):

        

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
            cursor.execute(f'UPDATE public."myBD" SET wlc_role=\'{role}\', wlc_role_t_or_f=\'{types}\' WHERE guild_id = \'{guild.id}\';')
            conn.commit()
            
            role1 = ctx.message.guild.get_role(role)
            
            emb = discord.Embed(
                title = 'Успешно!!!',
                description = f'Роль {role1.mention} была установлена как автоматическая роль с функцией `{types}`',
                colour = discord.Color.green(),
                timestamp = ctx.message.created_at
            )
            
            if ctx.guild.system_channel is not None:
                await ctx.guild.system_channel.send(embed = emb)
            elif ctx.guild.system_channel is None:
                await ctx.send(embed = emb)
        
        except Exception as e:
            print(f'[{ctx.message.created_at}] [{ctx.message.guild.name}] [{ctx.message.guild.owner}] - [{e}]')
        
        finally:
            if(conn):
                cursor.close()
                conn.close()
                
    
    async def cog_command_error(self, ctx: commands.Context, error: commands.CommandError):
        await ctx.send('Произошла ошибка: {}'.format(str(error)))
        print(f'[{ctx.message.created_at}] [{ctx.message.guild.name}] [{ctx.message.guild.owner}] - [{error}]')



def setup(bot):
    bot.add_cog(AuthoAddRole(bot))
