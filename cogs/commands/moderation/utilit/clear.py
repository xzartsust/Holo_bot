import discord 
from discord.ext import commands

class clear(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_messages = True)
    async def clear(self, ctx, arg: int):
        try:
            
            await ctx.channel.purge(limit = arg + 1)
        
        except Exception as e:
             print(f'[{ctx.message.created_at}] [{ctx.message.guild.name}] [{ctx.message.guild.owner}] - [{e}]')
        
    async def cog_command_error(self, ctx: commands.Context, error: commands.CommandError):
        await ctx.send('Произошла ошибка: {}'.format(str(error)))
        print(f'[{ctx.message.created_at}] [{ctx.message.guild.name}] [{ctx.message.guild.owner}] - [{error}]')


def setup(bot):
    bot.add_cog(clear(bot))