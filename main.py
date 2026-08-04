import tokens
from bot import Bot
from website_checker import WebsiteChecker
# Commands
from bot_commands.command_executor import CommandExecutor
from bot_commands.balance_command import BalanceCommand
from bot_commands.pay_command import PayCommand
from bot_commands.gamble_command import GambleCommand

# Check websites for words
checker = WebsiteChecker(
        url=tokens.URL,
        browser_profile=tokens.BROWSER_PROFILE
    )

# Register commands
command_executor = CommandExecutor()
command_executor.register_command(BalanceCommand("balance"))
command_executor.register_command(GambleCommand("gamble"))
command_executor.register_command(PayCommand("pay"))

# Create Bot
bot = Bot(
    website_checker=checker,
    command_executor=command_executor
)


bot.start()