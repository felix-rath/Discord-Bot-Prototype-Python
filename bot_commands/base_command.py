from discord import Message

class Command:

    def __init__(self, command_name: str):
        self.command_name = command_name

    async def on_command(self, message: Message , command: str, args: list[str]):
        pass
