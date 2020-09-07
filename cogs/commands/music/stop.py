import discord
from discord.ext import commands
from discord.utils import get
import youtube_dl


class MusicStop(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def stop(self, ctx):
        global voice
        
        voice = get(self.bot.voice_clients, guild = ctx.guild)

        if voice and voice.is_playing() and voice.is_connected():
            print('Music stopped')
            await voice.stop()
            await voice.disconnect()
            await voice.connect()
            await ctx.send('Music stopped')
        else:
            print('No music playing failed stopped')
            await ctx.send('No music playing failed stopped')


def setup(bot):
    bot.add_cog(MusicStop(bot))