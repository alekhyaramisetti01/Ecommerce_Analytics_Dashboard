DROP TABLE IF EXISTS product_catalog;

CREATE TABLE product_catalog (
    index INTEGER,
    sku_code TEXT,
    design_no TEXT,
    stock NUMERIC,
    category TEXT,
    size TEXT,
    color TEXT
);
