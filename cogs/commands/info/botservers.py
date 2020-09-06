import discord
from discord.ext import commands

class BotServers(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def botservers(self, ctx):
        emb=discord.Embed(
            description = f'Присутствует на {str(len(self.bot.guilds))} серверах',
            colour = discord.Color.blurple(),
            timestamp = ctx.message.created_at
        )
        await ctx.send(embed= emb)


def setup(bot):
    bot.add_cog(BotServers(bot))
