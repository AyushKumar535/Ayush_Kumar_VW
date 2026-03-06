CREATE DATABASE ecommerce_db;
USE ecommerce_db;

CREATE TABLE Orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    product_id INT,
    quantity INT,
    total_amount DECIMAL(10,2)
);

INSERT INTO Orders (order_id, customer_id, product_id, quantity, total_amount) VALUES
(1, 101, 201, 2, 500.00),
(2, 102, 202, 1, 150.00),
(3, 101, 203, 5, 1250.00),
(4, 103, 201, 3, 750.00),
(5, 101, 202, 1, 300.00),
(6, 102, 203, 10, 3000.00),
(7, 104, 204, 2, 400.00),
(8, 101, 205, 4, 2000.00),
(9, 103, 202, 6, 900.00),
(10, 101, 201, 1, 250.00);

SELECT 
    customer_id,
    SUM(total_amount) AS total_spent
FROM Orders
GROUP BY customer_id;

SELECT 
    customer_id,
    COUNT(order_id) AS num_orders
FROM Orders
GROUP BY customer_id;

SELECT 
    customer_id,
    COUNT(order_id) AS num_orders
FROM Orders
GROUP BY customer_id
HAVING COUNT(order_id) > 3;

SELECT 
    customer_id,
    SUM(total_amount) AS total_spent
FROM Orders
GROUP BY customer_id
HAVING SUM(total_amount) > 10000;

SELECT 
    product_id,
    SUM(quantity) AS total_quantity_sold
FROM Orders
GROUP BY product_id
HAVING SUM(quantity) > 100;