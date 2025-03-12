import time
from theta_server_entry import start_theta_terminal,stop_theta_terminal,get_available_options



def main():

    start_theta_terminal()
    time.sleep(5)
    get_available_options()
main()


