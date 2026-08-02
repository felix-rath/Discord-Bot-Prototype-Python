import tokens
from bot import Bot
from website_checker import WebsiteChecker
from games.game_manager import GameManager


checker = WebsiteChecker(
        url=tokens.URL,
        browser_profile=tokens.BROWSER_PROFILE
    )

game_manager = GameManager()

bot = Bot(
    website_checker=checker,
    game_manager=game_manager
)


bot.start()