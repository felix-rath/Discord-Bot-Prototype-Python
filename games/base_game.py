from discord import Message
# Base class only for inheritance
class BaseGame:

    def __init__(self, message: Message):
        self.message = message


    def start_game(self):
        print(self.__class__.__name__ + " no start_game method")