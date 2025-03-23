-- ✅ Revenue by Category (Domestic + International)
SELECT 
    pc.category,
    ROUND(SUM(a.amount), 2) AS domestic_revenue,
    ROUND(SUM(i.gross_amt), 2) AS international_revenue,
    ROUND(SUM(COALESCE(a.amount, 0)) + SUM(COALESCE(i.gross_amt, 0)), 2) AS total_revenue
FROM product_catalog pc
LEFT JOIN amazon_sales a ON pc.sku_code = a.sku
LEFT JOIN international_sales i ON pc.sku_code = i.sku
GROUP BY pc.category
ORDER BY total_revenue DESC;

-- ✅ Monthly Revenue Trend (Domestic only)
SELECT 
    DATE_TRUNC('month', a.date::DATE) AS month,
    ROUND(SUM(a.amount), 2) AS monthly_revenue
FROM amazon_sales a
WHERE a.status NOT ILIKE '%cancelled%'
GROUP BY month
ORDER BY month;
