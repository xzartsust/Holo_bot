import discord
from discord.ext import commands

class Avatar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ['av', 'a'])
    async def avatar(self, ctx):
        
        embed = discord.Embed(
            timestamp = ctx.message.created_at,
            colour = discord.Color.blue()
        )
        embed.set_image(
            url = ctx.message.author.avatar_url
        )
        await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(Avatar(bot))