import discord
from discord.ext import commands

class TotalUser(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def tuser(self, ctx):

        all_users = set([])
        for user in self.bot.get_all_members():
            all_users.add(user)
        await ctx.send('Total users in all my servers combined: ' + str(len(all_users)))

def setup(bot):
    bot.add_cog(TotalUser(bot))