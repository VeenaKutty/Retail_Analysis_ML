-- Revenue by Category
SELECT
    category,
    SUM(revenue) AS total_revenue
FROM inventory
GROUP BY category;


-- Regional Sales
SELECT
    region,
    SUM(units_sold) AS total_sales
FROM inventory
GROUP BY region;


-- Inventory Gap
SELECT
    product_id,
    SUM(stock_gap) AS stock_gap
FROM inventory
GROUP BY product_id;


-- Model Error
SELECT
    AVG(row_error) AS MAE
FROM inventory_predictions;