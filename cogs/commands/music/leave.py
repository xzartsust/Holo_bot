import discord
from discord.ext import commands
from discord.utils import get


class MusicLeave(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ['l', 'lea'])
    async def leave(self, ctx):
        global voice

        channel = ctx.message.author.voice.channel

        voice = get(self.bot.voice_clients, guild = ctx.guild)

        if voice and voice.is_connected():
            await voice.disconnect()
            await ctx.send(f'Bot disconnected with {channel}')
        else:
            await ctx.send('Bot is not in voice channel')


def setup(bot):
    bot.add_cog(MusicLeave(bot))