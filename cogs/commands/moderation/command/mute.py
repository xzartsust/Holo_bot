import discord
from discord.ext import commands
import psycopg2
import asyncio, asyncpg
import os

########################################################## Connect to SQL ###################################################


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


########################################################################################################################

class MuteCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator = True)
    async def mute(self, ctx, who: discord.Member, time: int, what: str, reason = None):
        
        guild = ctx.message.guild
        cursor.execute(f'SELECT role_id FROM public.mute_role WHERE guild_id = \'{guild.id}\';')
        role_mute = cursor.fetchone()
        conn.commit()
        print(role_mute[0])
        role = ctx.message.guild.get_role(role_mute[0])
        
        await ctx.channel.purge(limit = 1)
        
        print(f'[command.mute] От {ctx.author}, кого {who} роль {role}')
        
        if what == str('m'):
            if time >=1 and time <= 59:
                
                await ctx.send(f'--> {who} получил мут на {time}м. по причине: {reason}')

                await who.add_roles(role)
                await who.move_to(None)
                await asyncio.sleep(time * 60)
                await who.remove_roles(role)
                await ctx.send('Мут забраний')
        
        if what == str('h'):
            if time >= 1 and time <= 24:
                await ctx.send(f'--> {who} получил мут на {time}ч. по причине: {reason}')

                await who.add_roles(role)
                await who.move_to(None)
                await asyncio.sleep(time * 3600)
                await who.remove_roles(role)
                await ctx.send('Мут забраний')
        
        if what == str('d'):
            if time >= 1 and time <= 365:
                await ctx.send(f'--> {who} получил мут на {time}д. по причине: {reason}')

                await who.add_roles(role)
                await who.move_to(None)
                await asyncio.sleep(time * 86400)
                await who.remove_roles(role)
                await ctx.send('Мут забраний')
        
        if what == str('y'):
            if time >= 1:
                await ctx.send(f'--> {who} получил мут на {time}л. по причине: {reason}')

                await who.add_roles(role)
                await who.move_to(None)
                await asyncio.sleep(time * 31557600)
                await who.remove_roles(role)
                await ctx.send('Мут забраний') 


    @commands.command()
    @commands.has_permissions(administrator = True)
    async def muterole(self, ctx, role_id: discord.Role):
        guild = ctx.message.guild
        role = ctx.message.guild.get_role(role_id)

        cursor.execute(f'UPDATE public.mute_role SET role_id = \'{role_id}\' WHERE guild_id = \'{guild.id}\';')
        conn.commit()

        emb = discord.Embed(
            title= 'Успешно!',
            description = f'Роль {role.mention} была установленна для команды `mute`',
            timestamp = ctx.message.created_at
            )
        emb.set_footer(
            text = 'Запросил: ' + f'{ctx.author}',
            icon_url = ctx.author.avatar_url
            )
        
        if ctx.guild.system_channel is not None:
            await ctx.guild.system_channel.send(embed = emb)
        elif ctx.guild.system_channel is None:
            await ctx.send(embed = emb)

def setup(bot):
    bot.add_cog(MuteCommand(bot))