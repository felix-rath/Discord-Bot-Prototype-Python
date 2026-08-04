import tokens
from bot import Bot
from website_checker import WebsiteChecker
from bot_duels.duel_manager import DuelManager
# Commands
from bot_commands.command_executor import CommandExecutor
from bot_commands.balance_command import BalanceCommand
from bot_commands.pay_command import PayCommand
from bot_commands.gamble_command import GambleCommand
from bot_commands.duel_command import DuelCommand
from bot_commands.duel_accept_command import DuelAccept


# Check websites for words
checker = WebsiteChecker(
        url=tokens.URL,
        browser_profile=tokens.BROWSER_PROFILE
    )

# Command instances
duel_manager = DuelManager()

# Register commands
command_executor = CommandExecutor()
command_executor.register_command(BalanceCommand("balance"))
command_executor.register_command(GambleCommand("gamble"))
command_executor.register_command(PayCommand("pay"))
command_executor.register_command(DuelCommand("duel", duel_manager))
command_executor.register_command(DuelAccept("accept", duel_manager))

# Create Bot
bot = Bot(
    website_checker=checker,
    command_executor=command_executor
)


bot.start()