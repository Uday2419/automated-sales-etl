-- ==========================================
-- SALES ETL ANALYTICS
-- ==========================================


-- 1. Total Sales
SELECT
    SUM(sales) AS total_sales
FROM sales;


-- 2. Number of Orders
SELECT
    COUNT(DISTINCT order_id) AS total_orders
FROM sales;


-- 3. Total Customers
SELECT
    COUNT(DISTINCT customer_id) AS total_customers
FROM sales;


-- 4. Sales by Category
SELECT
    category,
    SUM(sales) AS total_sales
FROM sales
GROUP BY category
ORDER BY total_sales DESC;


-- 5. Sales by Region
SELECT
    region,
    SUM(sales) AS total_sales
FROM sales
GROUP BY region
ORDER BY total_sales DESC;


-- 6. Sales by Year
SELECT
    order_year,
    SUM(sales) AS total_sales
FROM sales
GROUP BY order_year
ORDER BY order_year;


-- 7. Sales by Month
SELECT
    order_year,
    order_month,
    order_month_name,
    SUM(sales) AS total_sales
FROM sales
GROUP BY
    order_year,
    order_month,
    order_month_name
ORDER BY
    order_year,
    order_month;


-- 8. Top 10 Products
SELECT
    product_name,
    SUM(sales) AS total_sales
FROM sales
GROUP BY product_name
ORDER BY total_sales DESC
LIMIT 10;


-- 9. Sales by Segment
SELECT
    segment,
    SUM(sales) AS total_sales
FROM sales
GROUP BY segment
ORDER BY total_sales DESC;


-- 10. Average Shipping Time
SELECT
    AVG(shipping_days) AS average_shipping_days
FROM sales;