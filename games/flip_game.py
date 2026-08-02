from games.base_game import BaseGame
import random
from user_data import money_manager

class FlipGame(BaseGame):

    def __init__(self, message):
          super().__init__(message)

        
    async def start_game(self):
            user_id = self.message.author.id
            display_name = self.message.author.display_name

            profit = random.randrange(2000)
            new_balance = await money_manager.add_balance(user_id, profit)
            await self.message.channel.send(
                f"WoW **{display_name}** hat **{abs(profit)}** gewonnen!!\n"
                f"💰 Neuer Kontostand: **{new_balance}**")