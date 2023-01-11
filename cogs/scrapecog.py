from discord.ext import commands
from discord import utils
import asyncio
from dotenv import load_dotenv
import os
import json

class Scrape(commands.Cog):
    def __init__(self, bot: commands.Bot, *args, **kwargs):
        load_dotenv()
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        # Replace 'channel-name' with the actual name of the channel
        channel = utils.get(self.bot.get_all_channels(), name='scrim-results')
        # Create an empty list to store the messages
        messages = []
        # Iterate over the messages in the channel
        async for message in channel.history(limit=None):
            # Convert the message to a dictionary and add it to the list
            message_dict = {
                'author': message.author.name,
                'content': message.content,
                'timestamp': message.created_at.isoformat()
            }
            messages.append(message_dict)
        # Write the list of messages to a JSON file
        with open('results.json', 'w') as f:
            json.dump(messages, f, indent=4)

async def setup(bot: commands.Bot):
    await bot.add_cog(Scrape(bot))
