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
        cursor.execute(f'SELECT role_for_mute FROM public."myBD" WHERE guild_id = \'{guild.id}\';')
        role_mute = cursor.fetchone()
        conn.commit()
        
        role = ctx.message.guild.get_role(role_mute[0])
        await ctx.channel.purge(limit = 1)

        await ctx.send(f'--> {who} получил мут по причине: {reason}')

        await who.add_roles(role)
        await who.move_to(None)

        '''
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
        '''

def setup(bot):
    bot.add_cog(MuteCommand(bot))