from bot_commands.command_executor import Command
from bot_games.flip_game import FlipGame
from bot_games.dice_game import DiceGame
from user_economy import economy_manager
import random


GAMBLE_PRICE = 1000
GAMBLE_GAMES = [DiceGame, FlipGame]


class GambleCommand(Command):

    async def on_command(self, message, command, args):

        if await economy_manager.remove_balance(message.author.id, GAMBLE_PRICE) is None:
            await message.channel.send(
                f"❌ **{message.author.display_name}**, du hast nicht genug Geld! Einsatz: **{GAMBLE_PRICE}** Coins")
            return

        r = random.randrange(len(GAMBLE_GAMES))
        game = GAMBLE_GAMES[r](message)
        await game.start_game()