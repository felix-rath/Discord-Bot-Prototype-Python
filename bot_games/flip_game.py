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

        new_balance = await economy_manager.add_balance(self.message.author.id, self.stake * 2)

        await self.message.channel.send(
            f"🎉 **{self.message.author.display_name}** hat **{abs(self.stake)} Coins** gewonnen!!\n")