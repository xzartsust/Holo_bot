import discord
from discord.ext import commands
from discord.ext import tasks

class MemberCount(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    update_required = False

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        update_required = True
        
    @commands.Cog.listener()
    async def on_member_remove(self, member: discord.Member):
        update_required = True
        
    @tasks.loop(minutes = 5)
    async def stats_update(self, ctx):
        if update_required:
            count_channel = self.bot.get_channel(727401938001461298) # CamelCase обычно обозначают Classы: https://www.python.org/dev/peps/pep-0008/#prescriptive-naming-conventions
            await count_channel.edit(name = f"Участников: {len(ctx.guild.members)}")
            update_required = False
            
    stats_update.start()

def setup(bot):
    bot.add_cog(MemberCount(bot))