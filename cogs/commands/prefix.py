import discord
from discord.ext import commands
import os
import asyncpg, asyncio



PREFIX=('.')





class prefix(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        pass
        

    @commands.Cog.listener()
    async def on_guild_remove(self,ctx):
        pass


    @commands.command()
    @commands.has_permissions(administrator=True)
    async def prefix(self, ctx, prefix):
        pass






def setup(bot):
    bot.add_cog(prefix(bot))

url = os.environ.get('db')