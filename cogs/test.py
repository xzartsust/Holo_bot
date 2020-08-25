import discord
from discord.ext import commands
import requests
import json
from discord.utils import get
import asyncio


class Test(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        
    @commands.command()
    @commands.is_owner()
    async def test(self, сtx, role: discord.Role = None):
        guildid = сtx.message.guild
        allvoice = guildid.voice_channels[0]
        alltext = guildid.text_channels[0]
        print(allvoice)
        print(alltext)
        await role.set_permissions(role, read_messages = True, send_messages = True, manage_channels = True, manage_roles = True)
        #await allvoice.set_permissions(role, connect = True, manage_channels = True, manage_roles = True)
        await сtx.send(f'{сtx.author.mention}, вы успешно установили {role.mention} права доступа во всех текстовых/голосовых каналах')

def setup(bot):
    bot.add_cog(Test(bot))