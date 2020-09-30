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

        try:
            
            all_users = set([])
            for user in self.bot.get_all_members():
                all_users.add(user)
            await ctx.send(f'```{len(all_users)}```')

        except Exception as e:
            print(f'[{ctx.message.created_at}] [{ctx.message.guild.name}] [{ctx.message.guild.owner}] - [{e}]')

    async def cog_command_error(self, ctx: commands.Context, error: commands.CommandError):
        await ctx.send('Произошла ошибка: {}'.format(str(error)))
        print(f'[{ctx.message.created_at}] [{ctx.message.guild.name}] [{ctx.message.guild.owner}] - [{error}]')
        
def setup(bot):
    bot.add_cog(TotalUser(bot))

bot_owner = os.environ.get('bot_owner')