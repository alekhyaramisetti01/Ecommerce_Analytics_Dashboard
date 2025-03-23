-- ✅ Stock vs. Total Orders (Domestic + International)

SELECT 
    pc.sku_code,
    pc.category,
    pc.stock,
    COALESCE(domestic.amazon_sales, 0) AS amazon_sales,
    COALESCE(international.international_sales, 0) AS international_sales,
    COALESCE(domestic.amazon_sales, 0) + COALESCE(international.international_sales, 0) AS total_orders
FROM product_catalog pc
LEFT JOIN (
    SELECT sku, COUNT(order_id) AS amazon_sales
    FROM amazon_sales
    GROUP BY sku
) domestic ON pc.sku_code = domestic.sku
LEFT JOIN (
    SELECT sku, SUM(pcs) AS international_sales
    FROM international_sales
    GROUP BY sku
) international ON pc.sku_code = international.sku
ORDER BY total_orders DESC
LIMIT 10;