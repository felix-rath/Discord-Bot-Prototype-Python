from bot_games.base_game import BaseGame
import random
from user_economy import economy_manager

class DiceGame(BaseGame): 

    DICE = [0, 1, 2, 5, 10, 25]

    WEIGHTS = [
        40,   # 0
        38,   # 1
        15,   # 2
        3,    # 5
        2,  # 10
        1   # 25
    ]
    
    DICE_EMOJI = [
        ":zero:",
        ":one:", 
        ":two:", 
        ":five:",
        ":one:" ":zero:",
        ":two:" ":five:",
    ]

    async def start_game(self):
        multiplier, dice_emoji = self._game_logic()

        profit = self._calculate_profit(multiplier)

        new_balance = await self._payout_profit(profit)

        await self._messager(profit, dice_emoji)


    def _game_logic(self):
        dice_index = random.choices(
            range(len(self.DICE)),
            weights=self.WEIGHTS,
            k=1)[0]

        dice_emoji = self.DICE_EMOJI[dice_index]
        multiplier = self.DICE[dice_index]
        return multiplier, dice_emoji

    
    def _calculate_profit(self, multiplier):
        profit = multiplier * self.stake
        return profit


    async def _payout_profit(self, profit):
        return await economy_manager.add_balance(self.message.author.id, profit)


    async def _messager(self, profit, dice_emoji):
        await self.message.channel.send(
            f"🎲 **{self.message.author.display_name}** hat **{dice_emoji}** gewürfelt: **{abs(profit)} Coins** Gewinn!\n")