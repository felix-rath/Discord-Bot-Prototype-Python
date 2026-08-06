from bot_commands.base_command import Command
from user_economy import economy_manager

class PayCommand(Command):

    async def on_command(self, message, command, args):
        if len(message.mentions) != 1:
            await message.channel.send("❌ Bitte erwähne genau **einen Benutzer**.")
            return

        if len(args) < 2:
            await message.channel.send("❌ Nutzung: `pay @User Betrag`")
            return

        try:
            amount = int(args[1])
        except ValueError:
            await message.channel.send("❌ Der **Betrag** muss eine Zahl sein.")
            return

        if amount <= 0:
            await message.channel.send("❌ Der Betrag muss größer als **0 Coins** sein.")
            return
        
        sender = message.author
        receiver = message.mentions[0]

        if await economy_manager.remove_balance(sender.id, amount) is None:
            await message.channel.send(
            f"❌ **{sender.display_name}**, du hast nicht genug **Coins**! ")
            return

        await economy_manager.add_balance(receiver.id, amount)

        await message.channel.send(
            f"💸 **{sender.display_name}** hat **{receiver.display_name}** "
            f"**{amount} Coins** gesendet!")