import discord
from discord.ext import commands
import pyttsx3

class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def test(self, ctx):
        
        tts = pyttsx3.init()
        voices = tts.getProperty('voices')
        tts.setProperty('voice', 'ru')
        tts.setProperty('rate', 150)    # Скорость в % (может быть > 100)
        tts.setProperty('volume', 1)
        for voice in voices:
            if voice.name == 'Microsoft Irina Desktop - Russian':
                tts.setProperty('voice', voice.id)
        tts.say('Привет')
        tts.runAndWait()

def setup(bot):
    bot.add_cog(Test(bot))