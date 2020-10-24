import discord
from discord.ext import commands

class LockPrivateChannel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def lock(self, ctx, member: discord.Member):
        try:
            voice_channel = ctx.message.author.voice.channel
            
            await voice_channel.set_permissions(member, connect = False)
            await member.move_to(None)

            emd = (discord.Embed(title = f'Приватный канал успешно заблокирован для {member.name}', 
                                colour = discord.Color.red()))
            await ctx.send(embed = emd)
        
        except Exception as e:
            print(f'[{ctx.message.created_at}] [{ctx.message.guild.name}] [{ctx.message.guild.owner}] - [{e}]')

    async def cog_command_error(self, ctx: commands.Context, error: commands.CommandError):
        #await ctx.send('Произошла ошибка: {}'.format(str(error)))
        if str(error) == str('\'NoneType\' object has no attribute \'channel\''):
                await ctx.send(f'{ctx.message.author.mention} вас нет в приватном голосовом канале, сначала создайте свой приватный голосовой канал')
        print(f'[{ctx.message.created_at}] [{ctx.message.guild.name}] [{ctx.message.guild.owner}] - [{error}]')
        

def setup(bot):
    bot.add_cog(LockPrivateChannel(bot))
