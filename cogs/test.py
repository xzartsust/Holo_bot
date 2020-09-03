import discord
from discord.ext import commands
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


class Test(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        
    @commands.command()
    @commands.is_owner()
    async def test(self, ctx, url: str):
        
        def endSong(self, guild, path):
            os.remove(path)

        guild_id = ctx.message.guild.id 
        
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            file = ydl.extract_info(url, download=True)
            guild = guild_id 
            path = str(file['title']) + "-" + str(file['id'] + ".mp3")
        
        channel_id = ctx.message.author.voice.channel

        channel1 = self.bot.get_channel(channel_id)                       
        voice_client = await channel1.connect()                                     
        
        voice_client.play(discord.FFmpegPCMAudio(path), after=lambda x: endSong(guild, path))
        voice_client.source = discord.PCMVolumeTransformer(voice_client.source, 1)
        
        while voice_client.is_playing(): 
            await asyncio.sleep(1)
        else:
            await voice_client.disconnect()
            print("Disconnected")
    
def setup(bot):
    bot.add_cog(Test(bot))
