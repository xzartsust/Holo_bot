import discord
from discord.ext import commands

class SendMessage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    @commands.has_permissions(administrator = True)
    async def send(self, ctx, *, text: str):
        
        await ctx.send(text)
        
def setup(bot):
    bot.add_cog(SendMessage(bot))
