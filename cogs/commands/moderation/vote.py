import discord
from discord.ext import commands

class Vote(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_messages = True)
    async def vote(self, ctx, caption: str = None, text: str = None, image: str = None,):
        
        await ctx.channel.purge(limit=1)

        if image is not None:
            emb = discord.Embed(
                title = f'{caption}',
                description = f'{text}',
                timestamp = ctx.message.created_at,
                colour = discord.Color.orange()
            )
            emb.set_footer(
                text = ctx.message.author,
                icon_url = ctx.message.author.avatar_url
            )
            emb.set_image(
                url = '{0}'.format(image)
            )
            message = await ctx.send(embed = emb)
            await message.add_reaction('<a:yes:754079238151340053>')
            await message.add_reaction('<a:no:754079450827718716>')
        if image is None:
            emb = discord.Embed(
                title = f'{caption}',
                description = f'{text}',
                timestamp = ctx.message.created_at,
                colour = discord.Color.orange()
            )
            emb.set_footer(
                text = ctx.message.author,
                icon_url = ctx.message.author.avatar_url
            )
            message = await ctx.send(embed = emb)
            await message.add_reaction('<a:yes:754079238151340053>')
            await message.add_reaction('<a:no:754079450827718716>')

def setup(bot):
    bot.add_cog(Vote(bot))