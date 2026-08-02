import user_data.data_saver as data_saver

def setup(bot):

    @bot.client.event
    async def on_message(message):

        if message.author == bot.client.user:
            return

        content = message.content.lower()
        user_id = message.author.id
        display_name = message.author.display_name

        await balance_command(message, content, user_id, display_name)
        await load_games(message)

    async def balance_command(message, content, user_id, display_name):
        if content.startswith("balance"):
            await message.channel.send(f"{display_name} hat {data_saver.load_money(message.author.id)}")

    async def load_games(message):
        await bot.game_manager.start(message)
