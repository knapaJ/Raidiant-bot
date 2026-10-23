import discord
from discord.ext import commands

from wowbot.cogs.CogBase import CogBase
from wowbot.utils import logger


class NoteTest(CogBase):

    @commands.slash_command()
    async def hello(self, ctx: discord.ApplicationContext, name: discord.Option(str, description="Name")):
        await ctx.respond(f'Hello! I am talking with a latency of {round(self.bot.latency * 1000)}ms [{name}]')
