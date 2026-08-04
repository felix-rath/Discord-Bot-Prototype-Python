from bot_games.base_game import BaseGame
import random
from user_data import economy_manager

class FlipGame(BaseGame):
        
    async def start_game(self):

            profit = random.randrange(2000)
            new_balance = await economy_manager.add_balance(self.message.author.id, profit)

            await self.message.channel.send(
                f"WoW **{self.message.author.display_name}** hat **{abs(profit)}** gewonnen!!\n"
                f"💰 Neuer Kontostand: **{new_balance}**")