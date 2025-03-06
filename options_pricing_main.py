from polygon import RESTClient
import QuantLib as ql
import yfinance as yf
from theta_server_entry import get_available_options, start_theta_terminal, stop_theta_terminal
import numpy as np


# SOR
RISK_FREE_RATE_SOR = 4.33



def main():

    # Start the Theta Terminal

    get_available_options()



    # Calculate option price


    ticker = yf.Ticker("MSFT")
    hist = ticker.history(period="10y")
    log_returns = np.log(hist['Close'] / hist['Close'].shift(1))
    volatility = log_returns.std() * np.sqrt(252)
    print(f"Annualized volatility: {volatility:.4f}")



    theta_process = start_theta_terminal()









    # When you're done, terminate the process
    stop_theta_terminal(theta_process)

main()








