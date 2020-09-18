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

    @commands.command(aliases = ['p', 'pl'])
    @commands.cooldown(1, 20, commands.BucketType.member)
    async def play(self, ctx, *, url: str):
        await def end(ctx):
            await ctx.send(1)

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
            info = ydl.extract_info(url, download = False)
            ydl.download([url])
            songname = info.get('title')
            
        for file in os.listdir("./"):
            if file.endswith(".mp3"):
                name = file
                print(f"Renamed File: {file}\n")
                os.rename(file, "song.mp3")

        try:
            
            voice.play(discord.FFmpegPCMAudio("song.mp3"), after = end(ctx))
            voice.source = discord.PCMVolumeTransformer(voice.source)
            voice.source.volume = 1

            nname = name.rsplit("-", 2)

            if songname is not None:
                await ctx.send(f"Сейчас играет: **{songname}**")
            else:
                await ctx.send(f"Сейчас играет: **{nname[0]}-{nname[1]}**")
        
        except Exception as e:
            print(e)
            await ctx.send('Простите я не могу проиграть эту музыку так как сейчас уже играет музыка. Подождите пока она зачиться <з или используйте команду `stop`')
            try:
                if song_there:
                    os.remove("song.mp3")
                    print("Removed song file")
            except PermissionError:
                print("Trying to delete song file, but it's being played")
                await ctx.send("ERROR: Music playing")
                return
        

def setup(bot):
    bot.add_cog(MusicPlay(bot))
