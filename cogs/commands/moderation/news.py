import discord
from discord.ext import commands

class news(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_messages = True)
    async def news(self, ctx, channel: discord.TextChannel, title: str, *, text: str):
        
        try:
            
            await ctx.channel.purge(limit = 1)
        
            emb = discord.Embed(
                title = f'{title}', 
                description=f'{text}', 
                colour= discord.Color.gold(), 
                timestamp=ctx.message.created_at)
            emb.set_footer(
                text=f'{ctx.message.author}' + ' создал эту новость!',
                icon_url = ctx.message.author.avatar_url
                )
        
            await channel.send(embed=emb)
        
        except Exception as e:
            print(f'[{ctx.message.created_at}] [{ctx.message.guild.name}] [{ctx.message.guild.owner}] - [{e}]')

    async def cog_command_error(self, ctx: commands.Context, error: commands.CommandError):
        await ctx.send('Произошла ошибка: {}'.format(str(error)))
        print(f'[{ctx.message.created_at}] [{ctx.message.guild.name}] [{ctx.message.guild.owner}] - [{error}]')


def setup(bot):
    bot.add_cog(news(bot))