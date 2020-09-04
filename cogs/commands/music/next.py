import discord 
from discord.ext import commands
from discord.utils import get


class MusicNext(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, aliases=['n', 'nex'])
    async def next(self, ctx):
        voice = get(self.bot.voice_clients, guild = ctx.guild)
        
        if voice and voice.is_playing():
            print("Playing Next Song")
            voice.stop()
            await ctx.send("Next Song")
        else:
            print("No music playing")
            await ctx.send("No music playing failed")

def setup(bot):
    bot.add_cog(MusicNext(bot))