from bot_commands.base_command import Command
from user_economy import economy_manager

class BalanceCommand(Command):

    async def on_command(self, message, command, args):
        balance = await economy_manager.get_balance(message.author.id)
        await message.channel.send(f"💰 **{message.author.display_name}**, dein Kontostand beträgt **{balance}** Coins.")