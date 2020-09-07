import discord
from discord.ext import commands
import time

class ping_serv(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):

        time_1 = time.perf_counter()
        await ctx.trigger_typing()
        time_2 = time.perf_counter()
        ping = round((time_2 - time_1) * 1000)
        emb= discord.Embed(description=f':ping_pong:Pong: {ping}ms',colour=discord.Color.blurple())
        emb.set_footer(text=ctx.message.author)
        await ctx.send(embed= emb)

def setup(bot):
    bot.add_cog(ping_serv(bot))