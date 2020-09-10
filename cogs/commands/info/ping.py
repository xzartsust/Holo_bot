import discord
from discord.ext import commands
import time

class ping_serv(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self._ping = bot.latency

    @commands.command()
    async def ping(self, ctx):

        emb= discord.Embed(description = ':ping_pong:Pong: {0._ping}ms'.format(self), colour=discord.Color.blurple())
        emb.set_footer(text = ctx.message.author)
        await ctx.send(embed = emb)

def setup(bot):
    bot.add_cog(ping_serv(bot))