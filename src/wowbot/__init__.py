import os
import dotenv
import discord

from wowbot.utils.logger import logger



bot = discord.Bot()

@bot.event
async def on_application_command(ctx: discord.ApplicationContext):
    logger.info(f"/{ctx.command.qualified_name} by {ctx.author.display_name}")

@bot.event
async def on_ready():
    logger.info(f"WoWbot ready!")

@bot.slash_command(name="ping", description="Test ping")
async def ping(ctx: discord.ApplicationContext):
    await ctx.respond("Pong!")
    logger.debug(f"Got pinged!")


def main() -> None:
    logger.debug(f"WoWbot loading...")
    dotenv.load_dotenv()
    logger.debug(f".env loaded")
    token = os.getenv("DC_TOKEN")
    if not token:
        logger.error("Token not found")
        exit(1)
    logger.debug(f"Discord token: <redacted>{token[-5:]}")

    logger.debug(f"WoWbot starting...")
    bot.run(token)






