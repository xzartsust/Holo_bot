import discord
from discord.ext import commands
from discord.utils import get
import youtube_dl


class MusicResume(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def resume(self, ctx):

        voice = get(self.bot.voice_clients, guild = ctx.guild)

        if voice and voice.is_paused():
            print('Resume music')
            voice.resume()
            await ctx.send('Music Resume')
        else:
            print('Music is not paused')
            await ctx.send('Music is not paused')


def setup(bot):
    bot.add_cog(MusicResume(bot))