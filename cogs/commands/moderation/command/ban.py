import discord
from discord.ext import commands
import typing


class BanUsers(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, members: commands.Greedy[discord.Member], delete_days: typing.Optional[int] = 0, *, reason: str = None):
        for member in members:
            await member.ban(delete_message_days=delete_days, reason=reason)

        if reason is None:
            await ctx.send(f'Пользователь {member} был забанен на этом сервера')
        elif reason is not None:
            await ctx.send(f'Пользователь {member} был забанен на этом сервера по причине {reason}')

def setup(bot):
    bot.add_cog(BanUsers(bot))