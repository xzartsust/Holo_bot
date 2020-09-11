import discord
from discord.ext import commands

class Vote(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions()
    async def vote(self, ctx, caption: str, *, text: str):
        
        emb = discord.Embed(
            title = f'{caption}',
            description = f'{text}',
            timestamp = ctx.message.created_at
        )
        await ctx.send(embed = emb)
        await ctx.message.add_reaction('<a:yes:754079238151340053>')
        await self.bot.add_reaction('<a:no:754079450827718716> ')

def setup(bot):
    bot.add_cog(Vote(bot))