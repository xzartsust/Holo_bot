import discord
from discord.ext import commands
import psycopg2
import asyncio, asyncpg
import os


class MuteCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator = True)
    async def mute(self, ctx, who: discord.Member, time: float, what: str, reason):
        role = ctx.message.guild.get_role(746275532039258122)
        
        print(f'[command.mute] От {ctx.author}, кого {who}')
        
        if what == str('s'):
            if time <= 1 :
                s = time * 60
                await ctx.send(f'--> {who} получил мут на {s} секунд по причине: {reason}')

                await who.add_roles(role)
                await who.move_to(None)
                await asyncio.sleep(s * 60)
                await who.remove_roles(role)
                await ctx.send('Мут забраний')
        
        if what == str('m'):
            if time >=1 and time <= 59:
                
                await ctx.send(f'--> {who} получил мут на {time} минут по причине: {reason}')

                await who.add_roles(role)
                await who.move_to(None)
                await asyncio.sleep(time * 60)
                await who.remove_roles(role)
                await ctx.send('Мут забраний')
        
        if what == str('h'):
            if time >= 1 and time <= 24:
                await ctx.send(f'--> {who} получил мут на {time} часов по причине: {reason}')

                await who.add_roles(role)
                await who.move_to(None)
                await asyncio.sleep(time * 3600)
                await who.remove_roles(role)
                await ctx.send('Мут забраний')
        
        if what == str('d'):
            if time >= 1 and time <= 365:
                await ctx.send(f'--> {who} получил мут на {time} дней по причине: {reason}')

                await who.add_roles(role)
                await who.move_to(None)
                await asyncio.sleep(time * 86400)
                await who.remove_roles(role)
                await ctx.send('Мут забраний')
        
        if what == str('y'):
            if time >= 1:
                await ctx.send(f'--> {who} получил мут на {time} лет по причине: {reason}')

                await who.add_roles(role)
                await who.move_to(None)
                await asyncio.sleep(time * 1557600)
                await who.remove_roles(role)
                await ctx.send('Мут забраний') 

def setup(bot):
    bot.add_cog(MuteCommand(bot))