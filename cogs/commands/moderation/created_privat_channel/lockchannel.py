import discord
from discord.ext import commands

class LockPrivateChannel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def lock(self, ctx, member):
        voice_channel = ctx.message.author.voice.channel
        if member is discord.Member:
            await voice_channel.set_permissions(member, connect = False)
            await member.move_to(None)
        elif member is discord.Role:
            await voice_channel.set_permissions(member, connect = False)

def setup(bot):
    bot.add_cog(LockPrivateChannel(bot))
