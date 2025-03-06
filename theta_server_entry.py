import subprocess
import time
import requests
import json
from config import THETA_USERNAME, THETA_PASSWORD, THETA_JAR_PATH

BASE_URL = "http://127.0.0.1:25510/v2/hist/option"
AUTH = (THETA_USERNAME, THETA_PASSWORD)

def start_theta_terminal():
    process = subprocess.Popen(['java', '-jar', THETA_JAR_PATH],
                               stdin=subprocess.PIPE,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE,
                               universal_newlines=True)
    time.sleep(5)
    process.stdin.write(f"{THETA_USERNAME}\n{THETA_PASSWORD}\n")
    process.stdin.flush()
    time.sleep(5)
    return process

def get_option_data(root, exp, strike, right, start_date, end_date):
    endpoint = f"{BASE_URL}/ohlc"
    params = {
        "root": root,
        "exp": exp,
        "strike": int(float(strike) * 1000),
        "right": right,
        "start_date": start_date,
        "end_date": end_date,
        "ivl": 60000  # 1-minute interval
    }
    response = requests.get(endpoint, params=params, auth=AUTH)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        print(f"Response: {response.text}")
        return None

# Example usage
option_data = get_option_data("AAPL", "20250321", 150.00, "C", "20250301", "20250305")
if option_data:
    print(json.dumps(option_data, indent=2))


# Start the Theta Terminal
theta_process = start_theta_terminal()

# Wait for the terminal to be fully initialized
time.sleep(10)

# Example usage
option_data = get_option_data("AAPL", "20250321", 150.00, "C", "20250301", "20250305")
if option_data:
    print(json.dumps(option_data, indent=2))

# When you're done, terminate the process
theta_process.terminate()
