import discord
from discord.ext import commands 
from discord.utils import get


class MusicJion(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ['j'])
    @commands.cooldown(1, 10, commands.BucketType.member)
    async def join(self, ctx):
        global voice

        try:
            channel = ctx.message.author.voice.channel
            
            voice = get(self.bot.voice_clients, guild = ctx.guild)
            
            if voice and voice.is_connected():
                await voice.move_to(channel)
                await ctx.send(f'Бот подключен к каналу {channel}')
            else:
                voice = await channel.connect()
                await ctx.send(f'Бот перешел к каналу {channel}')
        except Exception as e:
            print(e)  

def setup(bot):
    bot.add_cog(MusicJion(bot))