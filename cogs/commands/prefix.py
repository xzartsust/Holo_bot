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
        guildid= str(guild.id)
        conn = await asyncpg.connect(f'{url}')
        await conn.execute('INSERT INTO public.users(guild_id, prefix) VALUES ('+ f'{guildid}' + '.' +');' )
        await conn.close()
        

    @commands.Cog.listener()
    async def on_guild_remove(self):
        pass


    @commands.command()
    @commands.has_permissions(administrator=True)
    async def prefix(self, ctx, prefix):
        pass






def setup(bot):
    bot.add_cog(prefix(bot))

url = os.environ.get('DATABASE_URL')