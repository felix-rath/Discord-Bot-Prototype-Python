from games.flip_game import FlipGame
from games.dice_game import DiceGame
from user_data import money_manager
from user_data import daily_manager
import random

GAMBLE_COMMAND = "gamble"
GAMBLE_PRICE = 1000
GAMBLE_GAMES = [DiceGame, FlipGame]

class GameManager:

    def __init__(self):
        pass


    async def start(self, message):
        content = message.content.lower()
        if content.startswith(GAMBLE_COMMAND):
            await self.check_daily_reward(message)

            if await money_manager.remove_balance(message.author.id, GAMBLE_PRICE) is None:
                await message.channel.send(f"❌ **{message.author.display_name}**, du hast nicht genug Geld! Einsatz: **{GAMBLE_PRICE}** Coins")
                return
            
            r = random.randrange(len(GAMBLE_GAMES))
            game = GAMBLE_GAMES[r](message)
            await game.start_game()

    async def check_daily_reward(self, message):
        if await daily_manager.can_claim_daily(message.author.id) is True:
            await daily_manager.claim_daily(message.author.id)
            await message.channel.send(f"🎁 **{message.author.display_name}** hat sein Daily erhalten: **{daily_manager.DAILY_REWARD}** Coins! 💰")