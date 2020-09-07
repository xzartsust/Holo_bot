import discord
from discord.ext import commands
from discord.utils import get
import youtube_dl
import ctypes
import ctypes.util
import os
import asyncio

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}  


class MusicPlay(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def play(self, ctx, url: str = None):
        
        def endSong(self, guild, path):
            os.remove(path)

        guild_id = ctx.message.guild.id
        channel_id = ctx.message.author.voice.channel
        voice = get(self.bot.voice_clients, guild = ctx.guild)

        channel1 = self.bot.get_channel(channel_id.id)
        
        if voice.is_connected():
            await voice.disconnect()
            voice_client = await channel1.connect()
        else:
            voice_client = await channel1.connect()

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            file = ydl.extract_info(url, download=True)
            guild = guild_id 
            path = str(file['title']) + "-" + str(file['id'] + ".mp3")

        await ctx.send(f"Сейчас играет песня: **{file['title']}**")
                           
        voice_client.play(discord.FFmpegPCMAudio(path), after = lambda x: endSong(self, guild, path))
        voice_client.source = discord.PCMVolumeTransformer(voice_client.source, 1)
        
        while voice_client.is_playing(): 
            await asyncio.sleep(1)
        else:
            await voice_client.disconnect()
            await ctx.send(f"Песня **{file['title']}** закончилась")
            await channel1.connect()

def setup(bot):
    bot.add_cog(MusicPlay(bot))