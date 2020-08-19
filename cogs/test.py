import discord
from discord.ext import commands


class Test(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        
    @commands.command()
    @commands.is_owner()
    async def test(self, ctx):
        async for entry in ctx.message.guild.audit_logs(limit=100):
            print('{0.user} did {0.action} to {0.target}'.format(entry))

        async for entry in guild.audit_logs(action=discord.AuditLogAction.ban):
            print('{0.user} banned {0.target}'.format(entry))
        
def setup(bot):
    bot.add_cog(Test(bot))