from user_economy import daily_manager

def setup(bot):

    @bot.client.event
    async def on_message(message):

        if message.author == bot.client.user:
            return

        await check_daily_reward(message)
        await bot.command_executor.use_commands(message)

    async def check_daily_reward(message):
        if await daily_manager.claim_daily(message.author.id) is not None:
            await message.channel.send(
                f"🎁 **{message.author.display_name}** hat sein Daily erhalten: **{daily_manager.DAILY_REWARD}** Coins! 💰")