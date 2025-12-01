"""
Simple demonstration of the statistics library using data from a CSV file.

© 2025 Pau Erola, University of Bristol
"""

import sys
import pandas as pd
from stats_lib import mean, variance

# Get CSV filename from command line argument
if len(sys.argv) < 2:
    print("Usage: python example.py <csv_file>")
    sys.exit(1)

csv_file = sys.argv[1]

# Read data from CSV file
df = pd.read_csv(csv_file, header=None)

# Extract the temperature column as a list
data = df.values.flatten().tolist()

# Calculate mean
avg = mean(data)
print(f"Mean: {avg}")

# Calculate variance
var = variance(data)
print(f"Variance: {var}")

# Add test cases with None values
test_data_with_na = [1, 2, None, 4, 5, None, 7]
print(f"Mean (with NAs): {mean(test_data_with_na)}")
print(f"Variance (with NAs): {variance(test_data_with_na)}")
