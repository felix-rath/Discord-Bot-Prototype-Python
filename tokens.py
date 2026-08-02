from pathlib import Path

TOKEN = "PRIVATE TOKEN!" # discord bot token

SERVER_ID = 548519302555369494 # server id to only run on our server

ROLE_ID = 1532085427698143483 # discord role id to send the pm

KEYWORDS = ["Warteschlange", "Queue", "Virtuelle", "Neu", "Error", "Zugriff"] # keywords for the website word search

URL = "https://www.pokemoncenter.com/de-de" # link of the website 

BROWSER_PROFILE = Path(__file__).parent / "BrowserProfile" / "profile" # folder of the browser profile for playwright
