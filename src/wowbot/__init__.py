import os
import dotenv
import discord

from wowbot.utils.logger import logger


bot = discord.Bot()

@bot.event
async def on_application_command(ctx: discord.ApplicationContext):
    logger.info(f"/{ctx.command.qualified_name} by @{ctx.author.name}")

@bot.event
async def on_ready():
    logger.info(f"WoWbot ready!")
    await bot.change_presence(
        status=discord.Status.online,
        activity=discord.Activity(type=discord.ActivityType.listening, name="your mum")
    )

@bot.slash_command(name="ping", description_localizations={
    "cs": "Otestuj bota!",
    "en-US": "Test the bot!"
})
async def ping(ctx: discord.ApplicationContext):
    await ctx.respond('Pong!')

@bot.slash_command(name="crashme")
async def crashme(ctx: discord.ApplicationContext):
    raise Exception



def main() -> None:
    logger.debug(f"WoWbot loading...")
    dotenv.load_dotenv()
    logger.debug(f".env loaded")
    token = os.getenv("DC_TOKEN")
    if not token:
        logger.error("Token not found")
        exit(1)
    logger.debug(f"Discord token: <redacted>{token[-5:]}")

    sentry_dsn = os.getenv("SENTRY_DSN")
    if sentry_dsn is not None:
        logger.debug(f"Sentry DSN: @{sentry_dsn.split('@')[1]}")
        try:
            import wowbot.utils.sentry_setup as sentry_setup
            sentry_setup.setup_sentry(bot=bot, dsn=sentry_dsn)
        except ImportError:
            logger.error("Sentry not installed, but configured!")
            exit(1)
    else:
        logger.debug(f"Skipping Sentry")


    logger.debug(f"WoWbot starting...")
    bot.run(token)






