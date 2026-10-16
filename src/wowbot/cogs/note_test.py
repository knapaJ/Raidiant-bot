import discord
from discord.ext import commands
from wowbot.utils.logger import logger


class NoteTest(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx: commands.Context):
        await ctx.send(f'Hello! I am talking with a latency of {round(self.bot.latency * 1000)}ms')
