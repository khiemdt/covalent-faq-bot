import sys
import logging

import discord
from discord import Activity, ActivityType
from discord.ext import commands

import config
from utils import use_sentry
from constants import SENTRY_ENV_NAME


if __name__ == "__main__":
    # initialize bot params
    activity = Activity(type=ActivityType.playing, name="FAQ questions")
    bot = commands.Bot(command_prefix="faq.", help_command=None, intents=discord.Intents.default(), activity=activity)

    # init sentry SDK
    use_sentry(
        bot,
        dsn=config.SENTRY_API_KEY,
        environment=SENTRY_ENV_NAME,
    )

    # setup logger
    file_handler = logging.FileHandler(filename="covalent-faq.log")
    stdout_handler = logging.StreamHandler(sys.stdout)

    logging.basicConfig(
        level=logging.getLevelName(config.LOG_LEVEL),
        format="%(asctime)s %(levelname)s:%(message)s",
        handlers=[file_handler if config.LOG_TO_FILE else stdout_handler],
    )

    bot.load_extension("extensions.faq")
    bot.run(config.TOKEN)
