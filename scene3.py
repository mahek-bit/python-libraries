import numpy as np

sales = np.array([
[2000, 3000, 2500],
[1500, 2800, 2700],
[1800, 3200, 2900]
])

total = np.sum(sales, axis=1)

print("Daily Total Sales:")
print(total)