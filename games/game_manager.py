from games.flip_game import FlipGame
from games.dice_game import DiceGame
import random

GAMBLE_COMMAND = "gamble"
GAMBLE_GAMES = [DiceGame, FlipGame]

class GameManager:

    def __init__(self):
        pass


    async def start(self, message):
        content = message.content.lower()
        if content.startswith(GAMBLE_COMMAND):
            r = random.randrange(len(GAMBLE_GAMES))
            game = GAMBLE_GAMES[r](message)
            await game.start_game()