from discord.ext import commands

from wowbot.utils.logger import logger


class CogBase(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def setup(self):
        logger.info(f'Cog {self.__class__.__name__} registering into bot')
        self.bot.add_cog(self)
