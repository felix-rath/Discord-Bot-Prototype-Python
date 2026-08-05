from bot_commands.base_command import Command
import user_economy as economy_manager
import random

class DuelAccept(Command):

    def __init__(self, command_name, duel_manager):
        super().__init__(command_name)
        self.duel_manager = duel_manager

    async def on_command(self, message, command, args):
        opponent = message.author
        duel = self.duel_manager.get_duel_by_player(opponent.id)

        # Check for pending duel
        if duel is None:
            await message.channel.send(f"❌ **{opponent.display_name}**, du hast keine offene **Duell-Anfrage**.")
            return

        # variables
        challenger = duel.challenger
        amount = duel.amount
        balance_challenger = await economy_manager.get_balance(challenger.id)
        balance_opponent = await economy_manager.get_balance(opponent.id)

        # Check for enough money
        if balance_opponent < amount:
            await message.channel.send(f"❌ **{opponent.display_name}**, du hast nicht genug **Coins** für diesen Einsatz!")
            return
        if balance_challenger < amount:
            await message.channel.send(f"❌ **{challenger.display_name}** hat nicht genug **Coins** für dieses Duell!")
            return

        # Duel logic
        challenger_roll = random.randint(1, 100)
        opponent_roll = random.randint(1, 100)
        winner = None

        if challenger_roll > opponent_roll:
            winner = challenger
        elif opponent_roll > challenger_roll:
            winner = opponent
        else:
            await message.channel.send("🤝 Unentschieden!")
            self.duel_manager.remove_duel(duel)
            return

        # Handle money
        await economy_manager.remove_balance(challenger.id, amount)
        await economy_manager.remove_balance(opponent.id, amount)
        await economy_manager.add_balance(winner.id, amount*2)

        # Delete message to avoid chat spam
        await duel.message.delete()

        await message.channel.send(
            f"🎲 **Duell Ergebnis**\n\n"
            f"⚔️ **{challenger.display_name}**: **{challenger_roll}**\n"
            f"⚔️ **{opponent.display_name}**: **{opponent_roll}**\n\n"
            f"🏆 **{winner.display_name}** gewinnt!\n"
            f"💰 Gewinn: **{amount} Coins**")

        self.duel_manager.remove_duel(duel)