SELECT 
    pc.category,
    ROUND(
        100.0 * SUM(CASE WHEN a.status ILIKE '%cancelled%' THEN 1 ELSE 0 END)::DECIMAL / COUNT(*), 
        2
    ) AS cancellation_rate_pct
FROM amazon_sales a
JOIN product_catalog pc ON a.sku = pc.sku_code
GROUP BY pc.category
ORDER BY cancellation_rate_pct DESC;
