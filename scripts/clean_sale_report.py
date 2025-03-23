import pandas as pd
import os

# File paths
input_path = os.path.join("..", "data", "raw", "sale_report.csv")
output_path = os.path.join("..", "data", "processed", "sale_report_cleaned.csv")

# Load data
df = pd.read_csv(input_path)

# Clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Drop rows where SKU or Category is missing
df.dropna(subset=["sku_code", "category"], inplace=True)

# Convert stock to numeric (just in case it's not)
df["stock"] = pd.to_numeric(df["stock"], errors="coerce")

# Remove any duplicates based on SKU
df.drop_duplicates(subset=["sku_code"], inplace=True)

# Save cleaned file
df.to_csv(output_path, index=False)

print("✅ Cleaned Sale Report saved to:", output_path)
