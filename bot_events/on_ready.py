import discord
from bot_tasks.checker_loop import CheckerLoop

def setup(bot):

    @bot.client.event
    async def on_ready():
        print(f"Bot logged in as {bot.client.user}")
        if not bot.checker.started:
            await bot.checker.start()

            checker_loop = CheckerLoop(bot)
            checker_loop.checker_loop.start()