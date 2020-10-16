import discord
from discord.ext import commands


class KickUsers(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    #@commands.has_permissions(kick_members = True)
    async def kick(self, ctx, member: discord.Member, *, reason = None):
        try:
            
            await member.kick()

        except Exception as e:
            print(f'[{ctx.message.created_at}] [{ctx.message.guild.name}] [{ctx.message.guild.owner}] - [{e}]')
        
        if reason is None:

            kick = discord.Embed(
                title = f'{member} изгнанный из сервера :exclamation::exclamation:',
                timestamp = ctx.message.created_at,
                colour = discord.Color.red()
                )
            kick.add_field(
                name = 'Пользователь',
                value = f'{member.mention}'
                )
            kick.set_thumbnail(
                url = 'https://github.com/xzartsust/Tobi-Bot/blob/master/files/image/warn.jpg?raw=true'
                )
            kick.add_field(
                name = 'Модератор',
                value = f'{ctx.message.author.mention}'
                )
            kick.add_field(
                name = 'Причина',
                value = 'Не указана'
                )
            await ctx.send(embed = kick)
        
        elif reason is not None:
            
            kick = discord.Embed(
                title = f'{member} изгнанный из сервера :exclamation::exclamation:',
                timestamp = ctx.message.created_at,
                colour = discord.Color.red()
                )
            kick.add_field(
                name = 'Пользователь',
                value = f'{member.mention}'
                )
            kick.set_thumbnail(
                url = 'https://github.com/xzartsust/Tobi-Bot/blob/master/files/image/warn.jpg?raw=true'
                )
            kick.add_field(
                name = 'Модератор',
                value = f'{ctx.message.author.mention}'
                )
            kick.add_field(
                name = 'Причина',
                value = f'{reason}'
                )
            await ctx.send(embed = kick)

    async def cog_command_error(self, ctx: commands.Context, error: commands.CommandError):
        await ctx.send('Произошла ошибка: {}'.format(str(error)))
        print(f'[{ctx.message.created_at}] [{ctx.message.guild.name}] [{ctx.message.guild.owner}] - [{error}]')


def setup(bot):
    bot.add_cog(KickUsers(bot))
