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
print(f"Mean (with N/As): {avg}")

# Calculate variance
var = variance(data)
print(f"Variance with (N/As): {var}")
