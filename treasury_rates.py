import requests
import pandas as pd
from datetime import datetime


def get_treasury_rates():
    """
    Fetch the latest Treasury Bills, Notes, and Bonds rates

    Returns:
    dict: Dictionary with Treasury rates
    """
    # Base URL for the API
    base_url = "https://api.fiscaldata.treasury.gov/services/api/fiscal_service/v2/accounting/od/avg_interest_rates"

    # Initialize parameters
    params = {
        'page[size]': 20,
        'sort': '-record_date'  # Sort by date descending (newest first)
    }

    # Make the API request
    response = requests.get(base_url, params=params)

    # Default values in case API call fails
    treasury_rates = {
        'bills': None,
        'notes': None,
        'bonds': None,
        'date': None
    }

    # Check if request was successful
    if response.status_code == 200:
        data = response.json()

        # Convert to DataFrame
        if data['data']:
            df = pd.DataFrame(data['data'])

            # Convert date column to datetime
            df['record_date'] = pd.to_datetime(df['record_date'])

            # Convert interest rate to numeric
            df['avg_interest_rate_amt'] = pd.to_numeric(df['avg_interest_rate_amt'])

            # Get the most recent date
            latest_date = df['record_date'].max()
            treasury_rates['date'] = latest_date.strftime('%Y-%m-%d')

            # Filter for only the latest data
            latest_df = df[df['record_date'] == latest_date]

            # Get rates for Bills, Notes, and Bonds
            for security_type in ['Treasury Bills', 'Treasury Notes', 'Treasury Bonds']:
                matching_rows = latest_df[latest_df['security_desc'] == security_type]
                if not matching_rows.empty:
                    rate = matching_rows['avg_interest_rate_amt'].values[0]
                    if security_type == 'Treasury Bills':
                        treasury_rates['bills'] = rate
                    elif security_type == 'Treasury Notes':
                        treasury_rates['notes'] = rate
                    elif security_type == 'Treasury Bonds':
                        treasury_rates['bonds'] = rate
    else:
        print(f"Error: {response.status_code}")
        print(response.text)

    return treasury_rates




def main():

    treasury_rates = get_treasury_rates()
    print(treasury_rates)


main()
