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
    async def mute(self, ctx, who: discord.Member, time: float, reason):
        role = ctx.message.guild.get_role(746275532039258122)
        print(role)
        print(f'[command.mute] От {ctx.author}, кого {who}')
        if time < 1:
            s = time * 60
            await ctx.send(f'--> {who} получил мут на {s} cекунд по причине: {reason}')
        elif time > 1 or time >= 1:
            await ctx.send(f'--> {who} получил мут на {time} cекунд по причине: {reason}')
        
        await who.add_roles(role)
        await who.move_to(None)
        await asyncio.sleep(time * 60)
        await who.remove_roles(role)
        await ctx.send('Мут забраний')

def setup(bot):
    bot.add_cog(MuteCommand(bot))