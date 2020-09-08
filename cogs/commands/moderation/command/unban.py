import discord
from discord.ext import commands


class UnBanUser(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members = True, ban_members = True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_descriminator = member.split('#')
        
        try:
            for ban_entry in banned_users:
                user = ban_entry.user

            if (user.name, user.descriminator) == (member_name, member_descriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Пользователь {user.mention} был разбанен')
                return
        
        except discord.Forbidden:
            await ctx.send("У меня нет разрешения на разблокировку.")
            return
        except discord.HTTPException:
            await ctx.send("Разбан не удалось.")
            return

def setup(bot):
    bot.add_cog(UnBanUser(bot))