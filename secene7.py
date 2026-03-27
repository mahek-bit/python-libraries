import numpy as np

# Weekly rainfall data (in mm)
rainfall = np.array([12, 18, 25, 10, 20, 15, 22])

# Calculate mean, variance, and standard deviation
mean_rainfall = np.mean(rainfall)
variance_rainfall = np.var(rainfall)
std_rainfall = np.std(rainfall)

print("Weekly Rainfall Data:", rainfall)
print("Mean Rainfall:", mean_rainfall)
print("Variance of Rainfall:", variance_rainfall)
print("Standard Deviation of Rainfall:", std_rainfall)