import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import asyncio


def main():
    load_dotenv()

    bot = commands.Bot(command_prefix="?", intents=discord.Intents.all())

    @bot.event
    async def on_ready():
        print(f"Logged in as {bot.user}")

    @bot.event
    async def on_shutdown():
        print("caught!")

    asyncio.run(bot.load_extension("cogs.scrapecog"))

    token = os.environ.get("DISCORD_BOT_TOKEN")

    bot.run(token)

if __name__ == "__main__":
    main()
