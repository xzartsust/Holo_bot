import discord
from discord.ext import commands


class BotEvent(commands.Cog):
    def __init__(self, bot):
        self.bot= bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        await ctx.send(ctx.command.name + ' была вызвана некоректно')
    

def setup(bot):
    bot.add_cog(BotEvent(bot))
