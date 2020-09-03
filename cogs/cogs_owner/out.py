import discord 
from discord.ext import commands
import os

def is_owner(ctx):
    return ctx.author.id == bot_owner

class logout(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.command()
    @commands.is_owner()
    async def logout(self, ctx):
        await self.bot.logout()

def setup(bot):
    bot.add_cog(logout(bot))

bot_owner = os.environ.get('bot_owner')