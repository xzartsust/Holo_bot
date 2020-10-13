import discord
from discord.ext import commands
from discord.utils import get
import os
import asyncio, asyncpg
import psycopg2

database = os.environ.get('DATABASE')
user = os.environ.get('USER')
password = os.environ.get('PASSWORD')
host = os.environ.get('HOST')
port = os.environ.get('PORT')

conn = psycopg2.connect(
    database = f"{database}", 
    user = f"{user}", 
    password = f"{password}", 
    host = f"{host}", 
    port = "5432"
)

cursor = conn.cursor()

class PrivateChannel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
         
            
            cursor.execute(f'SELECT start_voice_channel FROM public."myBD" WHERE guild_id = \'{member.guild.id}\';')
            v_c = cursor.fetchone()
            voice_channel = v_c[0]
        
            cursor.execute(f'SELECT categori FROM public."myBD" WHERE guild_id = \'{member.guild.id}\';')
            c_c = cursor.fetchone()
            channel_category = c_c[0]

            if voice_channel is not None and channel_category is not None:
                if after.channel.id == voice_channel:
                    for guild in self.bot.guilds:
                        maincategori = get(guild.categories, id = channel_category)
                        channel2 = await guild.create_voice_channel(name = f'Приватний(member.display_name)', category = maincategori)
                        await channel2.set_permissions(member, connect = True, mute_members = True, move_members = True, manage_channels = True)
                        await member.move_to(channel2)
                        def check(self, x):
                            return len(channel2.members) == 0
                        await self.bot.wait_for('voice_channel_update', check = check)
                        await channel2.delete()
            else: 
                pass
        
        
            
    @commands.command()
    @commands.has_permissions(administrator = True)
    async def privatchnl(self, ctx, channel: int, categori: int):
        
        try:
            
            guild = ctx.message.guild
            cursor.execute(f'UPDATE public."myBD" SET start_voice_channel = \'{channel}\', categori = \'{categori}\' WHERE guild_id = \'{guild.id}\';')
            conn.commit()
            
            channel1 = self.bot.get_channel(channel)
            
            emb = (discord.Embed(title = 'Успешно!', 
                                 description = f'Канал `{channel1.name}` был установлен как начальний канал для создания частного голосового канала в категории `{channel1.category}`',
                                 colour = discord.Color.green(),
                                 timestamp = ctx.message.created_at)
                   .set_footer(text = ctx.message.author, icon_url = ctx.author.avatar_url))
            
            await ctx.send(embed = emb)
        
        except Exception as e:
            print(f'[{ctx.message.created_at}] [{ctx.message.guild.name}] [{ctx.message.guild.owner}] - [{e}]')
    
    async def cog_command_error(self, ctx: commands.Context, error: commands.CommandError):
        await ctx.send('Произошла ошибка: {}'.format(str(error)))
        print(f'[{ctx.message.created_at}] [{ctx.message.guild.name}] [{ctx.message.guild.owner}] - [{error}]')
        
def setup(bot):
    bot.add_cog(PrivateChannel(bot))
