from games.base_game import BaseGame
import random
import user_data.data_saver as data_saver

class DiceGame(BaseGame): 
    PRICE = 1000
    DICE = [2, 3, 4]
    DICE_EMOJI = [":two:", ":three:", ":four:"]

    def __init__(self, message):
        super().__init__(message)


    async def start_game(self):
        multiplier, dice_emoji = self._game_logic()

        profit = self._calculate_profit(multiplier)

        new_balance = self._payout_profit(profit)

        await self._messager(new_balance, profit, dice_emoji)


    def _game_logic(self):
        dice_index = random.randrange(len(self.DICE))
        direction = random.choice([-1, 1])

        dice_emoji = self.DICE_EMOJI[dice_index]
        multiplier = direction * self.DICE[dice_index]
        return multiplier, dice_emoji

    
    def _calculate_profit(self, multiplier):
        profit = multiplier * self.PRICE
        return profit


    def _payout_profit(self, profit):
        user_id = self.message.author.id
        new_balance = data_saver.load_money(user_id) + profit
        data_saver.set_money(user_id, new_balance)
        return new_balance


    async def _messager(self, new_balance, profit, dice_emoji):
        display_name = self.message.author.display_name
        await self.message.channel.send(
            f"**{display_name}** hat **{dice_emoji}** gewürfelt: {abs(profit)} **{'Gewinn' if profit > 0 else 'Verlust'}**\n"
            f"💰 Neuer Kontostand: **{new_balance}**"
        )