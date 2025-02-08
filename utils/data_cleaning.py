import os
import pandas as pd
import numpy as np

# Construct the absolute path
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_path = os.path.join(base_dir, 'data', 'feature_engineered_AI.csv')

# Load the feature-engineered dataset
df = pd.read_csv(data_path)

# Identify non-numeric columns
non_numeric_columns = df.select_dtypes(include=['object']).columns

# Replace non-numeric values with NaN
df[non_numeric_columns] = df[non_numeric_columns].apply(pd.to_numeric, errors='coerce')

# Fill NaN values with column mean
df.fillna(df.mean(), inplace=True)

# Save cleaned data
cleaned_data_path = os.path.join(base_dir, 'data', 'cleaned_feature_engineered_AI.csv')
df.to_csv(cleaned_data_path, index=False)

print(f"Cleaned data saved to {cleaned_data_path}")
