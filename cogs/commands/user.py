import discord
from discord.ext import commands
from datetime import datetime
import time



class user(commands.Cog):
    def __init__(self,bot):
        self.bot=bot

    @commands.command()
    async def user(self, ctx, member: discord.Member = None):
        member = ctx.author if not member else member
        roles =  [role for role in member.roles]


        time_to_join_in_discord = member.created_at
        time_to_join_in_server = member.joined_at
        now = datetime.now()
        delta_s = now - time_to_join_in_server
        delta_d= now - time_to_join_in_discord
        b= delta_d.days
        a = delta_s.days


        if member.bot is False and member.nick is not None:
            emb = discord.Embed(title=format(member), colour=discord.Color.green(), url=f'{member.avatar_url}', timestamp=ctx.message.created_at ,inline=False)
            emb.add_field(name='Присоединился к Discord',value=f'{member.created_at.strftime("%d.%m.%Y %H:%M")}\n ({b} дней)',inline=False)
            emb.add_field(name='Присоединился к серверу',value=f'{member.joined_at.strftime("%d.%m.%Y %H:%M")}\n ({a} дней)',inline=False)
            emb.add_field(name=f'Роли ({(len(roles))})',value=" ".join([role.mention for role in roles]), inline=False)
            emb.add_field(name='Самая высокая роль', value=str(member.top_role.mention), inline=False)
            emb.add_field(name='Айди', value=member.id, inline=False)

            if member.status == discord.Status.online:
                emb.add_field(name='Status', value=':green_circle: Онлайн', inline=False)
            elif member.status == discord.Status.dnd:
                emb.add_field(name='Status', value=':no_entry: Не беспокоить', inline=False)
            elif member.status == discord.Status.offline:
                emb.add_field(name='Status', value=':black_circle: Нет в сети', inline=False)
            elif member.status == discord.Status.idle:
                emb.add_field(name='Status', value=':crescent_moon: Отошол', inline=False)

            if member.activity is not None:
                emb.add_field(name='Кастом статус', value=member.activity, inline=False)
            else:
                emb.add_field(name='Кастом статус', value='Нету', inline=False)

            emb.set_thumbnail(url=member.avatar_url)
            emb.set_author(name=member.nick)
            emb.set_footer(text='Заптрос от: ' + f'{ctx.author}', icon_url=ctx.author.avatar_url)

            await ctx.channel.purge(limit=1)
            await ctx.send(embed=emb)

        if member.bot is False and member.nick is None:
            emb = discord.Embed(title=format(member), colour=discord.Color.green(), timestamp=ctx.message.created_at ,inline=False)
            emb.add_field(name='Присоединился к Discord', value=f'{member.created_at.strftime("%d.%m.%Y %H:%M")}\n ({b} дней)', inline=False)
            emb.add_field(name='Присоединился к серверу', value=f'{member.joined_at.strftime("%d.%m.%Y %H:%M")}\n ({a} дней)', inline=False)
            emb.add_field(name=f'Роли ({(len(roles))})',value=" ".join([role.mention for role in roles]), inline=False)
            emb.add_field(name='Самая высокая роль', value=str(member.top_role.mention), inline=False)
            emb.add_field(name='Айди', value=member.id, inline=False)

            if member.status == discord.Status.online:
                emb.add_field(name='Status', value=':green_circle: Онлайн', inline=False)
            elif member.status == discord.Status.dnd:
                emb.add_field(name='Status', value=':no_entry: Не беспокоить', inline=False)
            elif member.status == discord.Status.offline:
                emb.add_field(name='Status', value=':black_circle: Нет в сети', inline=False)
            elif member.status == discord.Status.idle:
                emb.add_field(name='Status', value=':crescent_moon: Отошол', inline=False)

            if member.activity is not None:
                emb.add_field(name='Кастом статус', value= member.activity,inline=False)
            else:
                emb.add_field(name='Кастом статус', value='Нету', inline=False)

            emb.set_thumbnail(url=member.avatar_url)
            emb.set_footer(text='Заптрос от: ' + f'{ctx.author}', icon_url=ctx.author.avatar_url)

            await ctx.channel.purge(limit=1)
            await ctx.send(embed=emb)

        if member.bot is True and member.nick is None:
            emb = discord.Embed(title=format(member), colour=discord.Color.green(), url=f'{member.avatar_url}', timestamp=ctx.message.created_at, inline=False)
            emb.add_field(name='Присоединился к Discord', value=f'{member.created_at.strftime("%d.%m.%Y %H:%M")}\n ({b} дней)', inline=False)
            emb.add_field(name='Присоединился к серверу', value=f'{member.joined_at.strftime("%d.%m.%Y %H:%M")}\n ({a} дней)', inline=False)
            emb.add_field(name=f'Роли ({(len(roles))})',value=" ".join([role.mention for role in roles]), inline=False)
            emb.add_field(name='Самая высокая роль', value=str(member.top_role.mention), inline=False)
            emb.add_field(name='Айди', value=member.id, inline=False)

            if member.status == discord.Status.online:
                emb.add_field(name='Status', value=':green_circle: Онлайн', inline=False)
            elif member.status == discord.Status.dnd:
                emb.add_field(name='Status', value=':no_entry: Не беспокоить', inline=False)
            elif member.status == discord.Status.offline:
                emb.add_field(name='Status', value=':black_circle: Нет в сети', inline=False)
            elif member.status == discord.Status.idle:
                emb.add_field(name='Status', value=':crescent_moon: Отошол', inline=False)

            emb.add_field(name='Кастомный статус', value=f'{member.activity}')

            emb.set_thumbnail(url=member.avatar_url)
            emb.set_footer(text='Заптрос от: ' + f'{ctx.author}', icon_url=ctx.author.avatar_url)

            await ctx.channel.purge(limit=1)
            await ctx.send(embed=emb)

        if member.bot is True and member.nick is not None:
            emb = discord.Embed(title=format(member), colour=discord.Color.green(), url=f'{member.avatar_url}', timestamp=ctx.message.created_at, inline=False)
            emb.add_field(name='Присоединился к Discord', value=f'{member.created_at.strftime("%d.%m.%Y %H:%M")}\n ({b} дней)', inline=False)
            emb.add_field(name='Присоединился к серверу', value=f'{member.joined_at.strftime("%d.%m.%Y %H:%M")}\n ({a} дней)', inline=False)
            emb.add_field(name=f'Роли ({(len(roles))})',value=" ".join([role.mention for role in roles]), inline=False)
            emb.add_field(name='Самая высокая роль', value=str(member.top_role.mention), inline=False)
            emb.add_field(name='Айди', value=member.id, inline=False)

            if member.status == discord.Status.online:
                emb.add_field(name='Status', value=':green_circle: Онлайн', inline=False)
            elif member.status == discord.Status.dnd:
                emb.add_field(name='Status', value=':no_entry: Не беспокоить', inline=False)
            elif member.status == discord.Status.offline:
                emb.add_field(name='Status', value=':black_circle: Нет в сети', inline=False)
            elif member.status == discord.Status.idle:
                emb.add_field(name='Status', value=':crescent_moon: Отошол', inline=False)

            emb.add_field(name='Кастомный статус',value=f'{member.activity}', inline=False)

            emb.set_thumbnail(url=member.avatar_url)
            emb.set_author(name=member.nick)
            emb.set_footer(text='Заптрос от: ' + f'{ctx.author}', icon_url=ctx.author.avatar_url)

            await ctx.channel.purge(limit=1)
            await ctx.send(embed=emb)


def setup(bot):
    bot.add_cog(user(bot))