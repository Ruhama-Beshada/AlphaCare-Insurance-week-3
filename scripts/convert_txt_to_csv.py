import pandas as pd
import os

# Paths
input_file = os.path.join('data', 'raw', 'MachineLearningRating_v3.txt')
output_file = os.path.join('data', 'processed', 'MachineLearningRating_v3.csv')

# Read pipe-delimited TXT
df = pd.read_csv(input_file, delimiter='|')

# Optional: remove extra spaces in string columns
df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

# Save as CSV
df.to_csv(output_file, index=False)

print(f"Conversion complete! CSV saved at '{output_file}'")
