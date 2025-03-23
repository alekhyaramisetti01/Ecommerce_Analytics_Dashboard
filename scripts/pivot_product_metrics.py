import pandas as pd
import os

# Load the original CSV
input_path = "../data/export/product_performance.csv"
output_path = "../data/export/product_metrics_long.csv"

df = pd.read_csv(input_path)

# Normalize column names (lowercase, strip spaces)
normalized_cols = [col.strip().lower() for col in df.columns]

# Map back to original names
column_map = dict(zip(normalized_cols, df.columns))

# Identify value columns dynamically
value_vars = [
    column_map[col] for col in normalized_cols
    if "sales" in col or "cost" in col
]

# Identify id columns (anything not in value_vars)
id_vars = [col for col in df.columns if col not in value_vars]

# Melt the dataframe
df_long = df.melt(
    id_vars=id_vars,
    value_vars=value_vars,
    var_name="metric_type",
    value_name="metric_value"
)

# Save result
os.makedirs("../data/export", exist_ok=True)
df_long.to_csv(output_path, index=False)

print(f"✅ Pivoted CSV saved to: {output_path}")
