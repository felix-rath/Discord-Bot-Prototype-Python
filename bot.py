import discord
import tokens
from website_checker import WebsiteChecker
import bot_events.on_message as on_message
import bot_events.on_ready as on_ready
from bot_commands.command_executor import CommandExecutor

class Bot:

    def __init__(self, website_checker: WebsiteChecker, command_executor: CommandExecutor):
        self.checker = website_checker
        self.command_executor = command_executor
        self.client = None
        self.is_queue = False

    def start(self):
        intents = self._create_intents()    
        self.client = discord.Client(intents=intents)

        self._load_events()
        
        self.client.run(token=tokens.TOKEN)

    def stop(self):
        if self.client is None:
            return
        self.client.close()

    ######CORE######

    def _create_intents(self):
        intents = discord.Intents.default()
        intents.message_content = True
        intents.members = True
        return intents

    def _load_events(self):
        on_ready.setup(self)
        on_message.setup(self)
