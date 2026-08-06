from bot_commands.command_executor import Command
from bot_games.flip_game import FlipGame
from bot_games.dice_game import DiceGame
from user_economy import economy_manager
import random


STANDARD_STAKE = 1000
MAX_STAKE = 10000
GAMBLE_GAMES = [DiceGame, FlipGame]


class GambleCommand(Command):

    async def on_command(self, message, command, args):

        stake = STANDARD_STAKE

        if len(args) > 0:
            try:
                stake = int(args[0])
            except ValueError:
                pass

        if stake > MAX_STAKE:
            await message.channel.send(
                f"❌ Der maximale Einsatz beträgt **{MAX_STAKE} Coins**.")
            return

        if await economy_manager.remove_balance(message.author.id, stake) is None:
            await message.channel.send(
                f"❌ **{message.author.display_name}**, du hast nicht genug Geld! Einsatz: **{stake}** Coins")
            return

        r = random.randrange(len(GAMBLE_GAMES))
        game = GAMBLE_GAMES[r](message, stake)
        await game.start_game()