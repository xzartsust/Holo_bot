import discord
from discord.ext import commands



class news(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def news(self, ctx, channel:discord.TextChannel, *, text):
        await ctx.channel.purge(limit=1)
        
        emb= discord.Embed(title='Новость!!!',description=f'{text}', colour= discord.Color.gold(),timestamp=ctx.message.created_at)
        emb.set_footer(text=f'{ctx.message.author}' + ' создал эту новость!')
        
        await channel.send(embed=emb)    





def setup(bot):
    bot.add_cog(news(bot))