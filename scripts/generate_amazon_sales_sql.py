import pandas as pd
import re

# Load cleaned CSV
df = pd.read_csv("../data/processed/amazon_sales_cleaned.csv")

# Sanitize column names
def clean_column(name):
    # Replace spaces and hyphens with underscores
    name = name.strip().lower().replace(' ', '_').replace('-', '_')
    # Remove any non-alphanumeric characters except underscore
    name = re.sub(r'[^\w_]', '', name)
    # If name starts with a digit, prepend "col_"
    if name and name[0].isdigit():
        name = 'col_' + name
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
table_name = "amazon_sales"
create_sql = f"""DROP TABLE IF EXISTS {table_name};

CREATE TABLE {table_name} (
    {columns}
);
"""

# Print and save
print(create_sql)
with open("../sql/create_tables/create_table_amazon_sales.sql", "w") as f:
    f.write(create_sql)

print("✅ Bulletproof SQL script saved to sql/create_tables/create_table_amazon_sales.sql")
