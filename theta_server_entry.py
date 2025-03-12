


BASE_URL = "http://127.0.0.1:25510/v2/"


import subprocess
import time

import os


def start_theta_terminal():
    # Import credentials directly within the function
    from config import THETA_USERNAME, THETA_PASSWORD, THETA_JAR_PATH

    try:
        # Check if jar file exists
        if not os.path.exists(THETA_JAR_PATH):
            print(f"Error: JAR file not found at {THETA_JAR_PATH}")
            return None

        # Start the Theta Terminal process
        process = subprocess.Popen(
            ['java', '-jar', THETA_JAR_PATH, THETA_USERNAME, THETA_PASSWORD],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True
        )

        # Give the terminal time to initialize
        print("Starting Theta Terminal...")

        # Check if process is still running
        if process.poll() is not None:
            # Process terminated, check for errors
            stderr = process.stderr.read()
            if stderr:
                print(f"Error starting Theta Terminal: {stderr}")
                return None

        print("Theta Terminal started successfully!")
        return process

    except Exception as e:
        print(f"Error launching Theta Terminal: {e}")
        return None


def stop_theta_terminal(process):
    if process is None:
        return

    try:
        # Terminate the process
        process.terminate()
        try:
            process.wait(timeout=5)  # Wait for it to terminate completely
        except subprocess.TimeoutExpired:
            print("Forcing termination...")
            process.kill()
        print("Theta Terminal stopped.")
    except Exception as e:
        print(f"Error stopping Theta Terminal: {e}")


if __name__ == "__main__":
    # Start the terminal
    terminal_process = start_theta_terminal()

    if terminal_process:
        try:
            # Keep the terminal running until user interrupts
            print("Theta Terminal is running. Press Ctrl+C to stop.")
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\nStopping Theta Terminal...")
        finally:
            stop_theta_terminal(terminal_process)




#
# def start_theta_terminal():
#     process = subprocess.Popen(['java', '-jar', THETA_JAR_PATH],
#                                stdin=subprocess.PIPE,
#                                stdout=subprocess.PIPE,
#                                stderr=subprocess.PIPE,
#                                universal_newlines=True)
#     time.sleep(5)
#     process.stdin.write(f"{THETA_USERNAME}\n{THETA_PASSWORD}\n")
#     process.stdin.flush()
#     # time.sleep(5)
#     return process
#
# def stop_theta_terminal(process):
#     try:
#         # Send 'exit' command to gracefully close the terminal
#         process.stdin.write("exit\n")
#         process.stdin.flush()
#         time.sleep(2)  # Allow time for the terminal to close
#     except Exception as e:
#         print(f"Error while sending exit command: {e}")
#
#     # Terminate the process if it's still running
#     process.terminate()
#     try:
#         process.wait(timeout=5)  # Wait for it to terminate completely
#     except subprocess.TimeoutExpired:
#         print("Forcing termination...")
#         process.kill()
#
# def get_available_options():
#     endpoint = "http://127.0.0.1:25510/v2/list/roots/option"
#     response = requests.get(endpoint, auth=(THETA_USERNAME, THETA_PASSWORD))
#     if response.status_code == 200:
#
#         available_options = response.json()
#         if available_options:
#             print(f"You have access to {len(available_options['response'])} options tickers on the Value tier:")
#             print("First few tickers:")
#             print(available_options['response'][:5])
#             print("...")
#             print("Last few tickers:")
#             print(available_options['response'][-5:])
#
#     else:
#         print(response.status_code)
