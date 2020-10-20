import discord
from discord.ext import commands

class LockPrivateChannel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def lock(self, ctx, member: discord.Member):
        voice_channel = ctx.message.author.channel
        await voice_channel.set_permissions(member, connect = False)
        await member.move_to(None)

def setup(bot):
    bot.add_cog(LockPrivateChannel(bot))
