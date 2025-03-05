
from polygon import RESTClient

from config import API_KEY

def get_option_data(client, underlying_symbol, expiration_date, min_strike, max_strike):
    options_chain = []
    for o in client.list_snapshot_options_chain(
        underlying_symbol,
        params={
            "expiration_date.gte": expiration_date,
            "strike_price.gte": min_strike,
            "strike_price.lte": max_strike,
        },
    ):
        options_chain.append(o)
    return options_chain

def main():
    # Initialize client with debug mode
    client = RESTClient(API_KEY, trace=True)

    # Set parameters
    underlying_symbol = "AAPL"
    expiration_date = "2024-03-16"
    min_strike = 29
    max_strike = 30

    # Get option data
    option_data = get_option_data(client, underlying_symbol, expiration_date, min_strike, max_strike)

    # Process and analyze the data
    for option in option_data:
        print(f"Option: {option}")

    print(f"Collected {len(option_data)} data points")

if __name__ == "__main__":
    main()

