import discord
from discord.ext import commands
import os

def is_owner(ctx):
    return ctx.author.id == bot_owner

class TotalUser(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def tuser(self, ctx):

        all_users = set([])
        for user in self.bot.get_all_members():
            all_users.add(user)
        await ctx.send(str(len(all_users)))

def setup(bot):
    bot.add_cog(TotalUser(bot))

bot_owner = os.environ.get('bot_owner')