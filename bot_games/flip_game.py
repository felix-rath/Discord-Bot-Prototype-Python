from bot_games.base_game import BaseGame
import random
from user_economy import economy_manager

class FlipGame(BaseGame):

    async def start_game(self):

        flip_number = random.randrange(0, 2)
        if flip_number == 0:
            await self.message.channel.send(
                f"🎉 **{self.message.author.display_name}** hat **{abs(self.stake)} Coins** verloren!!\n")
            return

        profit = self.stake * 2
        
        await economy_manager.add_balance(self.message.author.id, profit)

        await self.message.channel.send(
            f"🎉 **{self.message.author.display_name}** hat **{abs(profit)} Coins** gewonnen!!\n")