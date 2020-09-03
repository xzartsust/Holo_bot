import discord
from discord.ext import commands
from discord import utils
from discord.utils import get
import os


class InfoBot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def infobot(self, ctx):
        
        await ctx.channel.purge(limit = 1)

        d = self.bot.get_user('399851432221868033')
        
        print('Bot_owner: ', bot_owner)
        print(d)

        embed=discord.Embed(
            title=":information_source: BOT INFORMATION :information_source:",
            timestamp = ctx.message.created_at,
            colour = discord.Color.purple()
        )
        embed.add_field(
            name = 'Developer',
            value = f'```{self.bot.get_user(bot_owner)}```'
        )
        embed.add_field(
            name="Library",
            value="```discord.py```",
            inline=False
        )
        embed.add_field(
            name="Status",
            value="```Beta```", 
            inline=False
        )
        embed.add_field(
            name="Version",
            value="```0.0.3 Beta```",
            inline=True
        )
        embed.add_field(
            name="Website",
            value="https://github.com/xzartsust/Tobi-Bot",
            inline=False
        )
        embed.add_field(
            name="Official Bot Support Server",
            value="https://discord.gg/8f4KUp",
            inline=False
        )
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(InfoBot(bot))

bot_owner = os.environ.get('bot_owner')