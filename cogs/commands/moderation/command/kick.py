import discord
from discord.ext import commands


class KickUsers(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members = True)
    async def kick(self, ctx, member: discord.Member, *, reason = None):
        await member.kick()
        if reason is None:
            await ctx.send(f'Пользователь {member} был вигнал из сервера.')
        elif reason is not None:
            await ctx.send(f'Пользователь {member} был вигнал из сервера по причине {reason}')

def setup(bot):
    bot.add_cog(KickUsers(bot))