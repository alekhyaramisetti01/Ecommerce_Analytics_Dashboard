DROP TABLE IF EXISTS amazon_sales;

CREATE TABLE amazon_sales (
    index INTEGER,
    order_id TEXT,
    date TEXT,
    status TEXT,
    fulfilment TEXT,
    sales_channel TEXT,
    ship_service_level TEXT,
    style TEXT,
    sku TEXT,
    category TEXT,
    size TEXT,
    asin TEXT,
    courier_status TEXT,
    qty INTEGER,
    currency TEXT,
    amount NUMERIC,
    ship_city TEXT,
    ship_state TEXT,
    ship_postal_code NUMERIC,
    ship_country TEXT,
    b2b BOOLEAN,
    fulfilled_by TEXT
);
