from games.base_game import BaseGame
import random
import user_data.data_saver as data_saver

class FlipGame(BaseGame):

    def __init__(self, message):
          super().__init__(message)

        
    async def start_game(self):
            user_id = self.message.author.id
            display_name = self.message.author.display_name

            profit = random.randint(-10000, 10000)
            new_balance = data_saver.load_money(user_id) + profit
            data_saver.set_money(user_id, new_balance)
            await self.message.channel.send(
                f"WoW **{display_name}** hat **{abs(profit)}** "
                f"{'gewonnen' if profit > 0 else 'verloren'}!!\n"
                f"💰 Neuer Kontostand: **{new_balance}**")