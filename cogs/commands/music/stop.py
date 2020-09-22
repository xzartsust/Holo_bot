import discord
from discord.ext import commands
from discord.utils import get
import youtube_dl


class MusicStop(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ['s','st'])
    async def stop(self, ctx):
        global voice
        
        try:
            voice = get(self.bot.voice_clients, guild = ctx.guild)
            
            if voice and voice.is_playing() and voice.is_connected():
                voice.stop()
                await ctx.send('Музыка остановлена')
            else:
                await ctx.send('Музыка не воспроизводится, остановить не удалось')
        except Exception as e:
            print(e)

def setup(bot):
    bot.add_cog(MusicStop(bot))