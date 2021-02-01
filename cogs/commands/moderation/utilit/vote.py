import discord
from discord.ext import commands

class Vote(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_messages = True)
    async def vote(self, ctx, caption: str = None, text: str = None, image: str = None,):
        
        try:
            await ctx.channel.purge(limit = 1)

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
                await message.add_reaction('⭕')
                await message.add_reaction('❌')
        
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
                await message.add_reaction('⭕')
                await message.add_reaction('❌')
        
        except Exception as e:
            print(f'[{ctx.message.created_at}] [{ctx.message.guild.name}] [{ctx.message.guild.owner}] - [{e}]')


    async def cog_command_error(self, ctx: commands.Context, error: commands.CommandError):
        await ctx.send('Произошла ошибка: {}'.format(str(error)))
        print(f'[{ctx.message.created_at}] [{ctx.message.guild.name}] [{ctx.message.guild.owner}] - [{error}]')


def setup(bot):
    bot.add_cog(Vote(bot))