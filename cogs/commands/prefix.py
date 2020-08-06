import discord
from discord.ext import commands
import os
import asyncpg, asyncio

PREFIX=str('.')

url = os.environ.get('DATABASE_URL')

conn = asyncpg.connect(f'{url}')

class prefix(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        


    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        guildid= str(guild.id)

        cursor = conn.cursor()
        await cursor.execute(f'INSERT INTO prefixDB (guild_id, prefix) VALUES ({guildid},{PREFIX})')
    
        

    @commands.Cog.listener()
    async def on_guild_remove(self):
        pass


    @commands.command()
    @commands.has_permissions(administrator=True)
    async def prefix(self, ctx, prefix):
        pass






def setup(bot):
    bot.add_cog(prefix(bot))

