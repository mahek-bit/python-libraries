import numpy as np

prices = np.array([
[100, 200, 150],
[110, 210, 160],
[120, 220, 170]
])

# Daily change
change = prices[1] - prices[0]

print("Stock Price Change:")
print(change)