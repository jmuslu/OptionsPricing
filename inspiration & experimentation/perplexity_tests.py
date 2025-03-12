import numpy as np
import matplotlib.pyplot as plt

# Parameters for Bates model
V0 = 0.04
ThetaV = 0.05
Kappa = 1.0
SigmaV = 0.2
RhoSV = -0.7
Lambda = 2
MuJ = 0.02
SigmaJ = 0.08

# Simulate volatility path
np.random.seed(0)
dt = 1/252
T = 1
N = int(T/dt)
vol_path = np.zeros(N)
vol_path[0] = V0

for i in range(1, N):
    vol_path[i] = vol_path[i-1] + Kappa * (ThetaV - vol_path[i-1]) * dt + SigmaV * np.sqrt(vol_path[i-1]) * np.sqrt(dt) * np.random.normal(0, 1)

# Plot volatility path
plt.plot(vol_path)
plt.title('Volatility Path with Clustering')
plt.show()


# Generate price series with alternating high and low volatility
np.random.seed(0)
T = 1  # Time in years
N = 252  # Number of trading days
dt = T / N
price = np.zeros(N)
price[0] = 100  # Starting price

for i in range(1, N):
    if i % 2 == 0:  # High volatility on even days
        price[i] = price[i - 1] + np.random.normal(0, 0.3 * price[i - 1])
    else:  # Low volatility on odd days
        price[i] = price[i - 1] + np.random.normal(0, 0.05 * price[i - 1])

# Plot the price series without volatility details
plt.figure(figsize=(10, 6))
plt.plot(np.linspace(0, T, N), price, color='blue', label='Price')
plt.xlabel('Time (Years)')
plt.ylabel('Price')
plt.show()


