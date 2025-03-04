import requests
from config import API_KEY


BASE_URL = 'https://api.polygon.io'

def get_daily_open_close(symbol, date):
    endpoint = f'/v1/open-close/{symbol}/{date}'
    url = BASE_URL + endpoint
    params = {'apiKey': API_KEY}
    response = requests.get(url, params=params)
    return response.json()

def get_previous_close(symbol):
    endpoint = f'/v2/aggs/ticker/{symbol}/prev'
    url = BASE_URL + endpoint
    params = {'apiKey': API_KEY}
    response = requests.get(url, params=params)
    return response.json()

def get_aggregates(symbol, multiplier, timespan, from_date, to_date):
    endpoint = f'/v2/aggs/ticker/{symbol}/range/{multiplier}/{timespan}/{from_date}/{to_date}'
    url = BASE_URL + endpoint
    params = {'apiKey': API_KEY}
    response = requests.get(url, params=params)
    return response.json()

# Example usage
symbol = 'AAPL'
date = '2023-03-01'

daily_open_close = get_daily_open_close(symbol, date)
print("Daily Open/Close:", daily_open_close)

previous_close = get_previous_close(symbol)
print("Previous Close:", previous_close)

aggregates = get_aggregates(symbol, 1, 'day', '2023-01-01', '2023-03-01')
print("Aggregates:", aggregates)



