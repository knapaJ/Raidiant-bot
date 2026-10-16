import discord
import sentry_sdk

from wowbot.utils import logger


async def on_command_error(ctx: discord.ApplicationContext, error: discord.ApplicationCommandError) -> None:
    original_error = getattr(error, "original", error)

    with sentry_sdk.push_scope() as scope:
        scope.set_user({"id": ctx.author.id, "name": ctx.author.name})
        scope.set_tag("command", ctx.command.qualified_name if ctx.command else None)
        scope.set_extra("guild_id", ctx.guild_id)
        sentry_sdk.capture_exception(original_error)

    await ctx.respond(
        f"I encountered an error. Devs have been notified tho :)",
        ephemeral=True
    )



def setup_sentry(bot: discord.Bot, dsn: str, trace_sample: float=0.1, enable_logs: bool=True, environment: str='production'):
    sentry_sdk.init(
        dsn=dsn,
        traces_sample_rate=trace_sample,
        environment=environment,
        enable_logs=enable_logs,
    )
    logger.info(f"Attaching sentry to bot")
    bot.add_listener(on_command_error, "on_application_command_error")


