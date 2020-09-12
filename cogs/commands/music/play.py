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
    async def play(self, ctx, *, url):

        voice = get(self.bot.voice_clients, guild = ctx.guild)

        ydl_opts = {
            'format': 'bestaudio/best',
            'default_search': 'auto',
            'quiet': True,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }  

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            global path
            file = ydl.extract_info(url, download = True)
            path = str(file['title']) + "-" + str(file['id'] + ".mp3")

        await ctx.send(f"Сейчас играет песня: **{file['title']}**")
                           
        voice.play(discord.FFmpegPCMAudio(path), after = lambda x: print('Song End'))
        voice.source = discord.PCMVolumeTransformer(voice.source, 1)
        
        while voice.is_playing(): 
            await asyncio.sleep(1)
        else:
            pass

def setup(bot):
    bot.add_cog(MusicPlay(bot))
