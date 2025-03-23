import pandas as pd
import os

# File paths
input_path = os.path.join("..", "data", "raw", "international_sale_report.csv")
output_path = os.path.join("..", "data", "processed", "international_sales_cleaned.csv")

# Load data
df = pd.read_csv(input_path)

# Clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Convert DATE to datetime
df["date"] = pd.to_datetime(df["date"], errors="coerce")

# Clean numeric columns
df["pcs"] = pd.to_numeric(df["pcs"], errors="coerce")
df["rate"] = pd.to_numeric(df["rate"], errors="coerce")
df["gross_amt"] = pd.to_numeric(df["gross_amt"], errors="coerce")

# Drop rows missing essential values
df.dropna(subset=["sku", "date", "gross_amt"], inplace=True)

# Save cleaned version
df.to_csv(output_path, index=False)

print("✅ Cleaned International Sales saved to:", output_path)
