from schwab_auth import client
from datetime import datetime,timedelta
from theta_server_entry import start_theta_terminal


def main():

    start_theta_terminal()


    response = client.option_chains(
        symbol="NVDA",
        contractType="ALL",  # Get both calls and puts
        strikeCount=5,  # Get 5 strikes
        includeUnderlyingQuote=True,
        fromDate=datetime.now().strftime('%Y-%m-%d'),
        toDate=(datetime.now() + timedelta(days=30)).strftime('%Y-%m-%d'),
        strategy="SINGLE",
        range="ATM"  # At-the-money strikes
    )

    if response.ok:
        options_data = response.json()
        print("NVDA Options Chain:")
        for option in options_data['callExpDateMap']:
            print(f"Expiration: {option}")
            for strike in options_data['callExpDateMap'][option]:
                print(f"Strike: {strike}")
                print(options_data['callExpDateMap'][option][strike][0])

        for option in options_data['putExpDateMap']:
            print(f"Expiration: {option}")
            for strike in options_data['putExpDateMap'][option]:
                print(f"Strike: {strike}")
                print(options_data['putExpDateMap'][option][strike][0])
    else:
        print(f"Error: {response.status_code} - {response.text}")

    response = client.account_details_all(fields="positions")  # or None to exclude positions




main()




