-- ✅ Top 10 Products by Total Sales
SELECT 
    pc.sku_code,
    pc.category,
    SUM(COALESCE(a.amount, 0)) AS domestic_sales,
    SUM(COALESCE(i.gross_amt, 0)) AS international_sales,
    SUM(COALESCE(a.amount, 0)) + SUM(COALESCE(i.gross_amt, 0)) AS total_sales
FROM product_catalog pc
LEFT JOIN amazon_sales a ON pc.sku_code = a.sku
LEFT JOIN international_sales i ON pc.sku_code = i.sku
GROUP BY pc.sku_code, pc.category
ORDER BY total_sales DESC
LIMIT 10;
