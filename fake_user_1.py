import discord
import os
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

def main():

    bot = commands.Bot(command_prefix="?", intents=discord.Intents.all())
    
    @bot.event
    async def on_message(message):
        if message.content == '!join':
            # Join the voice channel the user is currently in
            channel = message.author.voice.channel
            if channel:
                await channel.connect()
                await message.channel.send(f'Joined {channel}')
            else:
                await message.channel.send('You are not in a voice channel')
        elif message.content == '!leave':
            # Leave the voice channel the bot is currently in
            vc = bot.voice_clients[0]
            if vc:
                await vc.disconnect()
                await message.channel.send(f'Left {vc.channel}')
            else:
                await message.channel.send('I am not in a voice channel')

    bot.run(os.environ.get('DISCORD_BOT_TOKEN_FAKE_1'))

if __name__ == "__main__":
    main()