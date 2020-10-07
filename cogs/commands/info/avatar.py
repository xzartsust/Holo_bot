import discord
from discord.ext import commands

class Avatar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ['av', 'a'])
    async def avatar(self, ctx, member: discord.Member):
        member = ctx.author if not member else member
        
        try:

            embed = discord.Embed(
                timestamp = ctx.message.created_at,
                colour = discord.Color.blue()
            )
            embed.set_image(
                url = member.avatar_url
            )
            await ctx.send(embed = embed)

        except Exception as e:
            print(f'[{ctx.message.created_at}] [{ctx.message.guild.name}] [{ctx.message.guild.owner}] - [{e}]')

def setup(bot):
    bot.add_cog(Avatar(bot))
