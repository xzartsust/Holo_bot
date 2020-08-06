import discord
from discord.ext import commands
import os
import asyncpg

PREFIX='.'


class prefix(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    



    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        guildid= str(guild.id)

        await self.bot.fetch(f'SELECT * FROM prefixDB WHERE guild_id = {guildid} AND prefix = {PREFIX}')

    @commands.Cog.listener()
    async def on_guild_remove(self):
        pass

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def prefix(self, ctx, prefix):
        pass






def setup(bot):
    bot.add_cog(prefix(bot))

