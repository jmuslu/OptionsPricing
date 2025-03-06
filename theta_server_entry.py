import subprocess
import time
import requests
import json
from config import THETA_USERNAME, THETA_PASSWORD, THETA_JAR_PATH

BASE_URL = "http://127.0.0.1:25510/v2/"
AUTH = (THETA_USERNAME, THETA_PASSWORD)

def start_theta_terminal():
    process = subprocess.Popen(['java', '-jar', THETA_JAR_PATH],
                               stdin=subprocess.PIPE,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE,
                               universal_newlines=True)
    # time.sleep(5)
    process.stdin.write(f"{THETA_USERNAME}\n{THETA_PASSWORD}\n")
    process.stdin.flush()
    # time.sleep(5)
    return process

def get_option_data(root, exp, strike, right, start_date, end_date):
    endpoint = f"{BASE_URL}bulk_snapshot/option/quote?root=AAPL&exp=20260116"
    params = {
        # "root": root,
        # "exp": exp,
        # "strike": int(float(strike) * 1000),
        # "right": right,
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

def stop_theta_terminal(process):
    try:
        # Send 'exit' command to gracefully close the terminal
        process.stdin.write("exit\n")
        process.stdin.flush()
        time.sleep(2)  # Allow time for the terminal to close
    except Exception as e:
        print(f"Error while sending exit command: {e}")

    # Terminate the process if it's still running
    process.terminate()
    try:
        process.wait(timeout=5)  # Wait for it to terminate completely
    except subprocess.TimeoutExpired:
        print("Forcing termination...")
        process.kill()



def get_available_options():
    endpoint = "http://127.0.0.1:25510/v2/list/roots/option"
    response = requests.get(endpoint, auth=(THETA_USERNAME, THETA_PASSWORD))
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        print(f"Response: {response.text}")
        return None

def main():
    available_options = get_available_options()
    if available_options:
        print(f"You have access to {len(available_options['response'])} options tickers on the Value tier:")
        print("First few tickers:")
        print(available_options['response'][:5])
        print("...")
        print("Last few tickers:")
        print(available_options['response'][-5:])


    # Start the Theta Terminal
    theta_process = start_theta_terminal()




    option_data = get_option_data("AAPL", "20250321", 150.00, "C", "20250301", "20250305")
    if option_data:
        print(json.dumps(option_data, indent=2))


    # When you're done, terminate the process
    stop_theta_terminal(theta_process)

main()