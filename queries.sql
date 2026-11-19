-- 1. Total revenue
SELECT ROUND(SUM(quantity * price), 2) AS total_revenue
FROM sales;

-- 2. Revenue by category
SELECT category,
       ROUND(SUM(quantity * price), 2) AS revenue
FROM sales
GROUP BY category
ORDER BY revenue DESC;

-- 3. Top 5 customers by spend
SELECT customer,
       ROUND(SUM(quantity * price), 2) AS total_spent
FROM sales
GROUP BY customer
ORDER BY total_spent DESC
LIMIT 5;

-- 4. Monthly revenue trend
SELECT substr(order_date, 1, 7) AS month,
       ROUND(SUM(quantity * price), 2) AS revenue
FROM sales
GROUP BY month
ORDER BY month;

-- 5. Best-selling products by units
SELECT product,
       SUM(quantity) AS units_sold
FROM sales
GROUP BY product
ORDER BY units_sold DESC
LIMIT 5;

-- 6. Average order value
SELECT ROUND(AVG(quantity * price), 2) AS avg_order_value
FROM sales;

-- 7. Orders per customer
SELECT customer, COUNT(*) AS num_orders
FROM sales
GROUP BY customer
ORDER BY num_orders DESC;

-- 8. Revenue by month and category (two-level grouping)
SELECT substr(order_date, 1, 7) AS month,
       category,
       ROUND(SUM(quantity * price), 2) AS revenue
FROM sales
GROUP BY month, category
ORDER BY month, revenue DESC;
