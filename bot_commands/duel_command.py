from bot_commands.base_command import Command
from bot_duels.duel import Duel
from user_data import economy_manager

class DuelCommand(Command):

    def __init__(self, command_name, duel_manager):
        super().__init__(command_name)
        self.duel_manager = duel_manager

    async def on_command(self, message, command, args):
        if len(message.mentions) != 1:
            await message.channel.send("❌ Bitte erwähne genau **einen Benutzer**.")
            return

        if len(args) < 2:
            await message.channel.send("❌ Nutzung: `duel @User Betrag`")
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

        balance_sender = await economy_manager.get_balance(sender.id)
        balance_receiver = await economy_manager.get_balance(receiver.id)

        if balance_sender < amount:
            await message.channel.send(f"❌ **{sender.display_name}**, du hast nicht genug **Coins** für diesen Einsatz!")
            return
        if balance_receiver < amount:
            await message.channel.send(f"❌ **{receiver.display_name}** hat nicht genug **Coins** für dieses Duell!")
            return
        
        duel = Duel(sender, receiver, amount)
        self.duel_manager.add_duel(duel)

        await message.channel.send(
            f"⚔️ **{sender.display_name}** fordert **{receiver.display_name}** zu einem Duell heraus!\n\n"
            f"💰 Einsatz: **{amount} Coins**\n\n"
            f"Schreibe `accept`, um anzunehmen.")



        