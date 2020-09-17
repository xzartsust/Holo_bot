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
            voice.pause()
            await ctx.send('Музыка на паузе')
        else:
            await ctx.send('Музыка не воспроизводится, не удалось приостановить')

def setup(bot):
    bot.add_cog(MusicPause(bot))