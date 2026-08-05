from discord import Message
from discord.abc import Messageable
# Base class only for inheritance
class BaseGame:

    def __init__(self, message: Message, stake):
        self.message = message
        self.stake = stake


    def start_game(self):
        print(self.__class__.__name__ + " no start_game method")