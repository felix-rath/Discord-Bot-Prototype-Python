

def setup(bot):

    @bot.client.event
    async def on_message(message):

        if message.author == bot.client.user:
            return

        content = message.content.lower()
        user_id = message.author.id
        display_name = message.author.display_name

        await bot.command_executor.use_commands(message)
