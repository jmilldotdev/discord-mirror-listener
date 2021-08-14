from discord.ext import commands


class ListenerCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


def setup(bot):
    bot.add_cog(ListenerCog(bot))
