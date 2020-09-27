import discord
from discord.ext import commands
import typing


class BanUsers(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, members: commands.Greedy[discord.Member], *, reason: str = None):
        try:
            
            for member in members:
                await member.ban(reason = reason)
        
        except Exception as e:
            print(f'[{ctx.message.created_at}] [{ctx.message.guild.name}] [{ctx.message.guild.owner}] - [{e}]')

        if reason is None:
            
            ban = discord.Embed(
                title = f'{member} был забанен :exclamation::exclamation:',
                timestamp = ctx.message.created_at,
                colour = discord.Color.red()
                )
            ban.add_field(
                name = 'Пользователь',
                value = f'{member.mention}'
                )
            ban.set_thumbnail(
                url = 'https://github.com/xzartsust/Tobi-Bot/blob/master/files/image/warn.jpg?raw=true'
                )
            ban.add_field(
                name = 'Модератор',
                value = f'{ctx.message.author.mention}'
                )
            ban.add_field(
                name = 'Причина',
                value = 'Не указана'
                )
            await ctx.send(embed = ban)
        
        else:
            
            ban = discord.Embed(
                title = f'{member} предупреждения :exclamation::exclamation:',
                timestamp = ctx.message.created_at,
                colour = discord.Color.red()
                )
            ban.add_field(
                name = 'Пользователь',
                value = f'{member.mention}'
                )
            ban.set_thumbnail(
                url = 'https://github.com/xzartsust/Tobi-Bot/blob/master/files/image/warn.jpg?raw=true'
                )
            ban.add_field(
                name = 'Модератор',
                value = f'{ctx.message.author.mention}'
                )
            ban.add_field(
                name = 'Причина',
                value = f'{reason}'
                )
            await ctx.send(embed = ban)
    async def cog_command_error(self, ctx: commands.Context, error: commands.CommandError):
        await ctx.send('Произошла ошибка: {}'.format(str(error)))
        print(f'[{ctx.message.created_at}] [{ctx.message.guild.name}] [{ctx.message.guild.owner}] - [{error}]')

def setup(bot):
    bot.add_cog(BanUsers(bot))