from user_data import money_manager

def setup(bot):

    @bot.client.event
    async def on_message(message):

        if message.author == bot.client.user:
            return

        content = message.content.lower()
        user_id = message.author.id
        display_name = message.author.display_name

        await balance_command(message)
        await load_games(message)

    async def balance_command(message):
        if message.content.startswith("balance"):
            balance = await money_manager.get_balance(message.author.id)
            await message.channel.send(f"💰 **{message.author.display_name}**, dein Kontostand beträgt **{balance}** Coins.")

    async def load_games(message):
        await bot.game_manager.start(message)
