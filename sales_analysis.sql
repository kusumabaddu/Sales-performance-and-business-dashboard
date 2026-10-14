
-- 1. Overall sales, profit, and profit margin
SELECT
    ROUND(SUM(sales)::numeric, 2) AS total_sales,
    ROUND(SUM(profit)::numeric, 2) AS total_profit,
    ROUND(
        100.0 * SUM(profit) / NULLIF(SUM(sales), 0),
        2
    ) AS profit_margin_pct
FROM superstore;

-- 2. Performance by category
SELECT
    category,
    ROUND(SUM(sales)::numeric, 2) AS total_sales,
    ROUND(SUM(profit)::numeric, 2) AS total_profit
FROM superstore
GROUP BY category
ORDER BY total_sales DESC;

-- 3. Performance by region
SELECT
    region,
    ROUND(SUM(sales)::numeric, 2) AS total_sales,
    ROUND(SUM(profit)::numeric, 2) AS total_profit,
    COUNT(DISTINCT order_id) AS unique_orders
FROM superstore
GROUP BY region
ORDER BY total_sales DESC;

-- 4. Top 10 products by sales
SELECT
    product_name,
    ROUND(SUM(sales)::numeric, 2) AS total_sales,
    ROUND(SUM(profit)::numeric, 2) AS total_profit
FROM superstore
GROUP BY product_name
ORDER BY total_sales DESC
LIMIT 10;