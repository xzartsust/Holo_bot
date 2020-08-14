import discord 
from discord.ext import commands

class clear(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def clear(self, ctx, arg: int):
        await ctx.channel.purge(limit= arg + 1)

    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            emb = discord.Embed(timestamp= ctx.message.created_at, title='Ошибка!!!', colour=discord.Color.red(), description='У вас нет прав на ету команду')
            emb.set_footer(text= ctx.message.author)
            await ctx.channel.purge(limit=1)
            await ctx.send(embed=emb)
        if isinstance(error, commands.MissingRequiredArgument):
            emb = discord.Embed(title='Ошибка!!!', colour=discord.Color.red(), description='Укажите сколько вы хотите удалить сообщений')
            await ctx.channel.purge(limit=1)

def setup(bot):
    bot.add_cog(clear(bot))