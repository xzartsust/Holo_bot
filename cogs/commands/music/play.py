import discord
from discord.ext import commands
from discord.utils import get
import youtube_dl
import ctypes
import ctypes.util
import os
import asyncio
from discord.ext.commands import Bot


class MusicPlay(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def play(self, ctx, *, url: str):

        voice = get(self.bot.voice_clients, guild = ctx.guild)

        song_there = os.path.isfile("song.mp3")
        try:
            if song_there:
                os.remove("song.mp3")
                print("Removed old song file")
        except PermissionError:
            print("Trying to delete song file, but it's being played")
            await ctx.send("ERROR: Music playing")
            return
        
        await ctx.send("Пожалуйста подождите загружается музыка")
        
        ydl_opts = {
            'format': 'bestaudio/best',
            'default_search': 'auto',
            'extractaudio': True,
            'audioformat': 'mp3',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
                }],
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            print("Downloading audio now\n")
            ydl.download([url])
            a = ydl.extract_info(url, download = False)

            
        for file in os.listdir("./"):
            if file.endswith(".mp3"):
                print(f"Renamed File: {file}\n")
                os.rename(file, "song.mp3")
                
        voice.play(discord.FFmpegPCMAudio("song.mp3"), after=lambda e: print("Song done!"))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 1
        
        await ctx.send(f"Playing: {a['title']}")
        print("playing\n")

def setup(bot):
    bot.add_cog(MusicPlay(bot))
