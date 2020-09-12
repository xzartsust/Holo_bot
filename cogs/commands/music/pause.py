import discord
from discord.ext import commands
import youtube_dl
from discord.utils import get


class MusicPause(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ['pa','pau'])
    async def pause(self, ctx):
        
        voice = get(self.bot.voice_clients, guild = ctx.guild)

        if voice and voice.is_playing():
            print('Music pause')
            voice.pause()
            await ctx.send('Music pause')
        else:
            print('Music not playing failed pause')
            await ctx.send('Music not playing failed pause')

def setup(bot):
    bot.add_cog(MusicPause(bot))