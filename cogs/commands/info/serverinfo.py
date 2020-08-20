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
        embed.set_thumbnail(
            url= guild.icon_url
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
        embed.add_field(
            name = 'Айди сервера',
            value = guild.id
        )
        if str(guild.region) == str('brazil'):
            embed.add_field(
                name = 'Регион',
                value = 'Бразилия',
                inline = False
            )
        elif str(guild.region) == str('russia'):
            embed.add_field(
                name = 'Регион',
                value = 'Россия',
                inline = False
            )
        elif str(guild.region) == str('hongkong'):
            embed.add_field(
                name = 'Регион',
                value = 'Гонконг',
                inline = False
            )
        elif str(guild.region) == str('india'):
            embed.add_field(
                name = 'Регион',
                value = 'Индия',
                inline = False
            )
        elif str(guild.region) == str('japan'):
            embed.add_field(
                name = 'Регион',
                value = 'Япония',
                inline = False
            )
        elif str(guild.region) == str('singapore'):
            embed.add_field(
                name = 'Регион',
                value = 'Сингапур',
                inline = False
            )
        elif str(guild.region) == str('southafrica'):
            embed.add_field(
                name = 'Регион',
                value = 'Южная Африка',
                inline = False
            )
        elif str(guild.region) == str('sydney'):
            embed.add_field(
                name = 'Регион',
                value = 'Сидней',
                inline = False
            )
        elif str(guild.region) == str('us-central'):
            embed.add_field(
                name = 'Регион',
                value = 'Центральное США',
                inline = False
            )
        elif str(guild.region) == str('us-east'):
            embed.add_field(
                name = 'Регион',
                value = 'Восточне США',
                inline = False
            )
        elif str(guild.region) == str('us-south'):
            embed.add_field(
                name = 'Регион',
                value = 'Северное США',
                inline = False
            )
        elif str(guild.region) == str('us-west'):
            embed.add_field(
                name = 'Регион',
                value = 'Западное США',
                inline = False
            )
        



        await ctx.send(embed = embed)




def setup(bot):
    bot.add_cog(ServerInfo(bot))