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
    async def mute(self, ctx, who: discord.Member, time: int, reason):
        role = ctx.message.guild.get_role(746275532039258122)
        print(role)
        print(f'[command.mute] От {ctx.author}, кого {who}')
        await ctx.send(f'--> {who} получил мут на {time} минут по причине: {reason}')
        await who.add_roles(role)
        await who.move_to(None)
        await asyncio.sleep(time * 60)
        await who.remove_roles(role)
        await ctx('Мут забраний')

def setup(bot):
    bot.add_cog(MuteCommand(bot))