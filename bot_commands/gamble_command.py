from bot_commands.command_executor import Command
from bot_games.flip_game import FlipGame
from bot_games.dice_game import DiceGame
from user_data import economy_manager
from user_data import daily_manager
import random


GAMBLE_PRICE = 1000
GAMBLE_GAMES = [DiceGame, FlipGame]


class GambleCommand(Command):

    async def on_command(self, message, command, args):

        await self.check_daily_reward(message)

        if await economy_manager.remove_balance(message.author.id, GAMBLE_PRICE) is None:
            await message.channel.send(
                f"❌ **{message.author.display_name}**, du hast nicht genug Geld! Einsatz: **{GAMBLE_PRICE}** Coins"
            )
            return

        r = random.randrange(len(GAMBLE_GAMES))
        game = GAMBLE_GAMES[r](message)
        await game.start_game()


    async def check_daily_reward(self, message):

        if await daily_manager.can_claim_daily(message.author.id) is True:
            await daily_manager.claim_daily(message.author.id)

            await message.channel.send(
                f"🎁 **{message.author.display_name}** hat sein Daily erhalten: **{daily_manager.DAILY_REWARD}** Coins! 💰"
            )