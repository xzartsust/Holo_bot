import discord
from discord.ext import commands
import youtube_dl
import ctypes
import ctypes.util
import os
import asyncio


class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    @commands.is_owner()
    async def test(self, ctx):
        guild = ctx.message.guild
         
        async for entry in guild.audit_logs(action = discord.AuditLogAction.invite_create):
            print('{0.user} {0.target}'.format(entry))
    

def setup(bot):
    bot.add_cog(Test(bot))
