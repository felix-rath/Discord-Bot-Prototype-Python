from games.base_game import BaseGame
import random
from user_data import money_manager

class DiceGame(BaseGame): 
    PRICE = 1000

    DICE = [
        0, 0, 0, 0, 0, 0,
        1, 1, 1, 1,
        2, 2,
        5,
        10,
        25
    ]
    
    DICE_EMOJI = [
        ":zero:", ":zero:", ":zero:", ":zero:", ":zero:", ":zero:",
        ":one:", ":one:", ":one:", ":one:",
        ":two:", ":two:",
        ":five:",
        ":one: :zero:",
        ":two: :five:"
    ]

    def __init__(self, message):
        super().__init__(message)


    async def start_game(self):
        multiplier, dice_emoji = self._game_logic()

        profit = self._calculate_profit(multiplier)

        new_balance = await self._payout_profit(profit)

        await self._messager(new_balance, profit, dice_emoji)


    def _game_logic(self):
        dice_index = random.randrange(len(self.DICE))

        dice_emoji = self.DICE_EMOJI[dice_index]
        multiplier = self.DICE[dice_index]
        return multiplier, dice_emoji

    
    def _calculate_profit(self, multiplier):
        profit = multiplier * self.PRICE
        return profit


    async def _payout_profit(self, profit):
        user_id = self.message.author.id
        return await money_manager.add_balance(user_id, profit)


    async def _messager(self, new_balance, profit, dice_emoji):
        display_name = self.message.author.display_name
        await self.message.channel.send(
            f"**{display_name}** hat **{dice_emoji}** gewürfelt: {abs(profit)} **{'Gewinn' if profit > 0 else 'Verlust'}**\n"
            f"💰 Neuer Kontostand: **{new_balance}**"
        )