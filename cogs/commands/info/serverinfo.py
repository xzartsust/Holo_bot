import discord
from discord.ext import commands
import os
import asyncpg, asyncio
import psycopg2
from discord import utils
from discord.utils import get


class ServerInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    

    @commands.command(aliases = ['si','is'])
    async def serverinfo(self, ctx):
        guild = ctx.message.guild

        embed = discord.Embed(
            title = f'Информация о сервере {guild.name}',
            colour = discord.Color.orange(),
            timestamp = ctx.message.created_at
        )
        embed.add_field(
            name = 'Owner сервера',
            value = guild.owner.mention,
            inline = False
        )
        embed.add_field(
            name = 'Названия сервера',
            value = guild.name,
            inline = False
        )



        await ctx.send(embed = embed)




def setup(bot):
    bot.add_cog(ServerInfo(bot))