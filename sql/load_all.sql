\copy amazon_sales FROM 'C:/Users/ramis/Ecommerce_Analytics_Dashboard/data/processed/amazon_sales_cleaned.csv' WITH (FORMAT csv, HEADER true)
\copy product_catalog FROM 'C:/Users/ramis/Ecommerce_Analytics_Dashboard/data/processed/sale_report_cleaned.csv' WITH (FORMAT csv, HEADER true)
\copy international_sales FROM 'C:/Users/ramis/Ecommerce_Analytics_Dashboard/data/processed/international_sales_cleaned.csv' WITH (FORMAT csv, HEADER true)
