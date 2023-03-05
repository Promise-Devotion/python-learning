import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import shapiro

data = [31, 59, 73, 52, 60, 68, 57, 42, 61, 46, 56, 62, 36, 11, 25, 15, 4]

# Create histogram
plt.hist(data, bins=5)
plt.title("Histogram of Runs Data")
plt.xlabel("Runs")
plt.ylabel("Frequency")
plt.show()

# Perform Shapiro-Wilk test
stat, p = shapiro(data)
print("Shapiro-Wilk test results:")
print("Test statistic:", stat)
print("p-value:", p)

if p > 0.05:
    print("The data is normally distributed.")
else:
    print("The data is not normally distributed.")