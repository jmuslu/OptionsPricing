import subprocess
import time
import requests
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

        available_options = response.json()
        if available_options:
            print(f"You have access to {len(available_options['response'])} options tickers on the Value tier:")
            print("First few tickers:")
            print(available_options['response'][:5])
            print("...")
            print("Last few tickers:")
            print(available_options['response'][-5:])

    else:
        print(response.status_code)


def main():


    start_theta_terminal()
    time.sleep(5)
    get_available_options()

main()