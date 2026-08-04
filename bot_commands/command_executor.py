from bot_commands.base_command import Command
from discord import Message

class CommandExecutor:

    def __init__(self):
        self.registered_commands: list[Command] = []

    def register_command(self, command_executor: Command):
        self.registered_commands.append(command_executor)

    # Strip discord message to have easier command creation
    # Check each message for all registered commands
    async def use_commands(self, message: Message):
        for command in self.registered_commands:
            content_array = message.content.split()
            command_name = content_array[0]
            content_array.pop(0)

            if command_name.lower() == command.command_name.lower():
                await command.on_command(message, command_name.lower(), content_array)