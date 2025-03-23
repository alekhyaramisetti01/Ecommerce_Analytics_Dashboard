DROP TABLE IF EXISTS international_sales;

CREATE TABLE international_sales (
    index INTEGER,
    date TEXT,
    months TEXT,
    customer TEXT,
    style TEXT,
    sku TEXT,
    size TEXT,
    pcs NUMERIC,
    rate NUMERIC,
    gross_amt NUMERIC
);
