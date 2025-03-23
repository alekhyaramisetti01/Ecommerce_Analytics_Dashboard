import pandas as pd
import os

# Set file paths
input_path = os.path.join("..", "data", "raw", "amazon_sales_report.csv")
output_path = os.path.join("..", "data", "processed", "amazon_sales_cleaned.csv")

# Load the data
df = pd.read_csv(input_path)

# Clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Drop unnecessary columns
columns_to_drop = ['unnamed:_22', 'promotion-ids']
df.drop(columns=columns_to_drop, inplace=True, errors='ignore')

# Convert data types
df['date'] = pd.to_datetime(df['date'], errors='coerce')
df['amount'] = pd.to_numeric(df['amount'], errors='coerce')

# Drop rows with missing essential values
df.dropna(subset=['order_id', 'date', 'amount'], inplace=True)

# Save cleaned file
df.to_csv(output_path, index=False)

print("✅ Cleaned data saved to:", output_path)
