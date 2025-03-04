from polygon import RESTClient
from datetime import datetime, timedelta
from config import API_KEY

def get_stock_data(client, symbol, start_date, end_date):
    return client.stocks_equities_aggregates(
        symbol, 1, "day", start_date, end_date, adjusted=True
    )

def get_option_data(client, option_symbol, start_date, end_date):
    return client.options_aggregates(
        option_symbol, 1, "day", start_date, end_date
    )

# Initialize client
client = RESTClient(API_KEY)

# Set date range
end_date = datetime.now().strftime("%Y-%m-%d")
start_date = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d")

# Get stock data
stock_symbol = "AAPL"
stock_data = get_stock_data(client, stock_symbol, start_date, end_date)

# Get option data (example for a specific contract)
option_symbol = "O:AAPL250117C00150000"
option_data = get_option_data(client, option_symbol, start_date, end_date)

# Process and analyze the data
for stock_bar, option_bar in zip(stock_data.results, option_data.results):
    stock_volume = stock_bar.v
    stock_price = stock_bar.c
    option_price = option_bar.c
    date = datetime.fromtimestamp(stock_bar.t / 1000).strftime("%Y-%m-%d")
    print(f"Date: {date}, Stock Volume: {stock_volume}, Stock Price: {stock_price}, Option Price: {option_price}")
