import pandas as pd
import re

# Load your cleaned CSV
df = pd.read_csv("../data/processed/sale_report_cleaned.csv")

# Clean column names: remove spaces, hyphens, special characters
def clean_column(name):
    name = name.strip().lower().replace(" ", "_").replace("-", "_")
    name = re.sub(r"[^\w_]", "", name)
    if name and name[0].isdigit():
        name = "col_" + name
    return name

df.columns = [clean_column(col) for col in df.columns]

# Infer PostgreSQL-compatible data types
def infer_pg_type(dtype):
    if pd.api.types.is_integer_dtype(dtype):
        return "INTEGER"
    elif pd.api.types.is_float_dtype(dtype):
        return "NUMERIC"
    elif pd.api.types.is_bool_dtype(dtype):
        return "BOOLEAN"
    elif pd.api.types.is_datetime64_any_dtype(dtype):
        return "DATE"
    else:
        return "TEXT"

# Generate SQL column definitions
columns = ",\n    ".join(
    f"{col} {infer_pg_type(dtype)}"
    for col, dtype in df.dtypes.items()
)

# Final CREATE TABLE statement
table_name = "product_catalog"
create_sql = f"""DROP TABLE IF EXISTS {table_name};

CREATE TABLE {table_name} (
    {columns}
);
"""

# Print and save to file
print(create_sql)
with open("../sql/create_tables/create_table_product_catalog.sql", "w") as f:
    f.write(create_sql)

print("✅ SQL script saved to sql/create_tables/create_table_product_catalog.sql")
