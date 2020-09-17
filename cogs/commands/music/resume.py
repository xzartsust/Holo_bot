import discord
from discord.ext import commands
from discord.utils import get
import youtube_dl


class MusicResume(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ['r','res'])
    async def resume(self, ctx):

        voice = get(self.bot.voice_clients, guild = ctx.guild)

        if voice and voice.is_paused():
            voice.resume()
            await ctx.send('Воспроизведения музыки возобновилось')
        else:
            await ctx.send('Музыка не на паузе')


def setup(bot):
    bot.add_cog(MusicResume(bot))