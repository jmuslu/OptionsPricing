import subprocess
import time
from config import THETA_USERNAME, THETA_PASSWORD, THETA_JAR_PATH


def start_theta_terminal():
    process = subprocess.Popen(['java', '-jar', THETA_JAR_PATH],
                               stdin=subprocess.PIPE,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE,
                               universal_newlines=True)

    # Wait for the login prompt
    time.sleep(2)

    # Send username
    process.stdin.write(THETA_USERNAME + '\n')
    process.stdin.flush()

    # Wait briefly
    time.sleep(0.5)

    # Send password
    process.stdin.write(THETA_PASSWORD + '\n')
    process.stdin.flush()

    return process


# Start the Theta Terminal
theta_process = start_theta_terminal()

# Your main code here
# ...

# When you're done, you can terminate the process
# theta_process.terminate()

