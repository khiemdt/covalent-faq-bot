import gettext

from discord import Embed
from discord.ext import commands

import config
from constants import GREEN


_ = gettext.gettext
en = gettext.translation("base", localedir="locales", languages=["en"])
ar = gettext.translation("base", localedir="locales", languages=["ar"])
en.install()

locales = {
    # AR
    config.AR_CHANNEL_ID: ar,
}


def resolve_language(function):
    """ async wrapper for changing language on the fly"""

    async def wrapper(ctx):
        if ctx.channel.id in locales.keys():
            locale = locales[ctx.channel.id]
        else:
            locale = en
        locale.install()
        _ = locale.gettext
        # ensure that bot is allowed to send messages in channel
        if ctx.channel.id in config.ALLOWED_CHANNELS_IDS:
            return await function(ctx, _)

    return wrapper


@commands.command("help")
@resolve_language
async def help_command(ctx, _):
    widget = Embed(description=_("HELP_DESCRIPTION"), color=GREEN, title=_("HELP_TITLE"))
    widget.set_thumbnail(url="https://covalenthq.s3.eu-north-1.amazonaws.com/Covalent_Logomark_DeepBlue.png")
    widget.add_field(name="faq.covalent", value=_("HELP_COVALENT"), inline=False)
    widget.add_field(name="faq.tasks", value=_("HELP_TASKS"), inline=False)
    widget.add_field(name="faq.rewards", value=_("HELP_REWARDS"), inline=False)
    widget.add_field(name="faq.navigation", value=_("HELP_NAVIGATION"), inline=False)
    widget.add_field(name="faq.pinned", value=_("HELP_PINNED"), inline=False)
    await ctx.send(embed=widget)


@commands.command("covalent", aliases=["cov", "company"])
@resolve_language
async def covalent(ctx, _):
    widget = Embed(title=_("COVALENT_TITLE"), color=GREEN, description=_("COVALENT_DESCRIPTION"))
    widget.set_thumbnail(url="https://covalenthq.s3.eu-north-1.amazonaws.com/Covalent_Logomark_DeepBlue.png")
    widget.add_field(name=_("COVALENT_FIELD1_NAME"), value=_("COVALENT_FIELD1_VALUE"))
    await ctx.send(embed=widget)


@commands.command("tasks", aliases=["potions"])
@resolve_language
async def tasks(ctx, _):
    widget = Embed(title=_("TASKS_TITLE"), color=GREEN, description=_("TASKS_DESCRIPTION"))
    widget.set_thumbnail(url="https://covalenthq.s3.eu-north-1.amazonaws.com/Covalent_Logomark_DeepBlue.png")
    widget.add_field(name=_("TASKS_FIELD1_NAME"), value=_("TASKS_FIELD1_VALUE"), inline=False)
    widget.add_field(name=_("TASKS_FIELD2_NAME"), value=_("TASKS_FIELD2_VALUE"), inline=False)
    widget.add_field(name=_("TASKS_FIELD3_NAME"), value=_("TASKS_FIELD3_VALUE"), inline=False)
    widget.add_field(name=_("TASKS_FIELD4_NAME"), value=_("TASKS_FIELD4_VALUE"), inline=False)
    widget.add_field(name=_("TASKS_FIELD5_NAME"), value=_("TASKS_FIELD5_VALUE"), inline=False)
    widget.add_field(name=_("TASKS_FIELD6_NAME"), value=_("TASKS_FIELD6_VALUE"), inline=False)
    widget.add_field(name=_("TASKS_FIELD7_NAME"), value=_("TASKS_FIELD7_VALUE"), inline=False)
    widget.add_field(name=_("TASKS_FIELD8_NAME"), value=_("TASKS_FIELD8_VALUE"), inline=False)
    await ctx.send(embed=widget)


@commands.command("rewards", aliases=["reward"])
@resolve_language
async def rewards(ctx, _):
    widget = Embed(title=_("REWARDS_TITLE"), color=GREEN, description=_("REWARDS_DESCRIPTION"))
    widget.set_thumbnail(url="https://covalenthq.s3.eu-north-1.amazonaws.com/Covalent_Logomark_DeepBlue.png")
    widget.add_field(name=_("REWARDS_FIELD1_NAME"), value=_("REWARDS_FIELD1_VALUE"), inline=False)
    widget.add_field(name=_("REWARDS_FIELD2_NAME"), value=_("REWARDS_FIELD2_VALUE"), inline=False)
    widget.add_field(name=_("REWARDS_FIELD3_NAME"), value=_("REWARDS_FIELD3_VALUE"), inline=False)
    widget.add_field(name=_("REWARDS_FIELD4_NAME"), value=_("REWARDS_FIELD4_VALUE"), inline=False)
    widget.add_field(name=_("REWARDS_FIELD5_NAME"), value=_("REWARDS_FIELD5_VALUE"), inline=False)
    await ctx.send(embed=widget)


@commands.command("navigation")
@resolve_language
async def navigation(ctx, _):
    widget = Embed(title=_("NAVIGATION_TITLE"), color=GREEN, description=_("NAVIGATION_TITLE_DESCRIPTION"))
    widget.set_thumbnail(url="https://covalenthq.s3.eu-north-1.amazonaws.com/Covalent_Logomark_DeepBlue.png")
    widget.add_field(name=_("NAVIGATION_FIELD1_NAME"), value=_("NAVIGATION_FIELD1_VALUE"), inline=False)
    widget.add_field(name=_("NAVIGATION_FIELD2_NAME"), value=_("NAVIGATION_FIELD2_VALUE"), inline=False)
    await ctx.send(embed=widget)


@commands.command("pinned")
@resolve_language
async def pinned(ctx, _):
    widget = Embed(color=GREEN)
    widget.set_author(
        name=_("Pinned Messages"),
        icon_url="https://covalenthq.s3.eu-north-1.amazonaws.com/Covalent_Logomark_DeepBlue.png",
    )
    widget.set_image(url="https://covalenthq.s3.eu-north-1.amazonaws.com/pinned.png")
    await ctx.send(embed=widget)


def setup(bot):
    bot.add_command(help_command)
    bot.add_command(covalent)
    bot.add_command(tasks)
    bot.add_command(rewards)
    bot.add_command(navigation)
    bot.add_command(pinned)
