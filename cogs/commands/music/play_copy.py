import discord
from discord.ext import commands
from discord.utils import get
import youtube_dl
import os
import shutil

players = {}

class MusicPlay(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def join(self, ctx):
        channel = ctx.message.author.voice.channel

        voice = get(self.bot.voice_clients, guild = ctx.guild)

        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await channel.connect()

    @commands.command()
    async def leave(self, ctx):
        voice = get(self.bot.voice_clients, guild = ctx.guild)
        await voice.disconnect()

    @commands.command()
    async def play(self, ctx, url):
        guild = ctx.message.guild
        voice = get(self.bot.voice_clients, guild = ctx.guild)
        player = await voice.create_ytdl_player(url)
        players[guild.id] = player
        player.start()


def setup(bot):
    bot.add_cog(MusicPlay(bot))