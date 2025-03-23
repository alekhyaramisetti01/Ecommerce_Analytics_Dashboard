import os
import pandas as pd
import psycopg2

# DB connection settings
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="1234567890",
    host="localhost",
    port="5432"
)

# Folder paths
query_folder = "../sql/kpi"
export_folder = "../data/export"
os.makedirs(export_folder, exist_ok=True)

# Loop through each .sql file in /sql/kpis
for file in os.listdir(query_folder):
    if file.endswith(".sql"):
        kpi_name = file.replace(".sql", "")
        query_path = os.path.join(query_folder, file)
        with open(query_path, "r") as f:
            query = f.read()

        try:
            df = pd.read_sql(query, conn)
            output_path = os.path.join(export_folder, f"{kpi_name}.csv")
            df.to_csv(output_path, index=False)
            print(f"✅ Exported {kpi_name} to {output_path}")
        except Exception as e:
            print(f"❌ Failed to export {kpi_name}: {e}")

conn.close()
