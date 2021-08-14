from discord.ext import commands
from cogwatch import watch

from listener import config, const

TOKEN = config.DISCORD_TOKEN


class ListenerBot(commands.Bot):
    def __init__(self) -> None:
        commands.Bot.__init__(self, command_prefix=config.COMMAND_PREFIX)

    @watch(path=const.COGS_PATH, preload=True, default_logger=False)
    async def on_ready(self) -> None:
        print("Running...")


def start() -> None:
    print("Launching bot")
    bot = ListenerBot()
    bot.run(TOKEN)
