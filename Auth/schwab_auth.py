import schwabdev
from credentials import SCHWAB_APP_KEY, SCHWAB_APP_SECRET, REDIRECT_HOST

client = schwabdev.Client(SCHWAB_APP_KEY, SCHWAB_APP_SECRET, REDIRECT_HOST, "tokens.json")





