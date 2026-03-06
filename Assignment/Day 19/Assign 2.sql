CREATE DATABASE retail_db;
USE retail_db;

CREATE TABLE Customers (
    customer_id INT PRIMARY KEY,
    name VARCHAR(100),
    city VARCHAR(50)
);

CREATE TABLE Orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    total_amount DECIMAL(10,2),
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);

CREATE TABLE Products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    price DECIMAL(10,2)
);

CREATE TABLE Order_Items (
    order_item_id INT PRIMARY KEY,
    order_id INT,
    product_id INT,
    quantity INT,
    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);

INSERT INTO Customers VALUES
(1, 'Alice', 'New York'),
(2, 'Bob', 'Los Angeles'),
(3, 'Ayush', 'Chicago'),
(4, 'David', 'Houston'),
(5, 'Eva', 'Phoenix');

INSERT INTO Products VALUES
(1, 'Laptop', 1000.00),
(2, 'Smartphone', 500.00),
(3, 'Headphones', 100.00),
(4, 'Keyboard', 50.00),
(5, 'Mouse', 25.00);

INSERT INTO Orders VALUES
(1, 1, '2026-01-10', 1500.00),
(2, 2, '2026-01-12', 500.00),
(3, 1, '2026-02-05', 100.00),
(4, 3, '2026-02-10', 200.00),
(5, 1, '2026-03-01', 1200.00),
(6, 4, '2026-03-05', 500.00),
(7, 1, '2026-03-20', 300.00);

INSERT INTO Order_Items VALUES
(1, 1, 1, 1),
(2, 1, 2, 1),
(3, 2, 2, 1),
(4, 3, 3, 1),
(5, 4, 4, 2),
(6, 5, 1, 1),
(7, 6, 2, 1),
(8, 7, 5, 12);

SELECT c.customer_id, c.name, COUNT(o.order_id) AS total_orders
FROM Customers c
JOIN Orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.name
HAVING COUNT(o.order_id) > 3;

SELECT c.customer_id, c.name, SUM(o.total_amount) AS total_spent
FROM Customers c
JOIN Orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.name
ORDER BY total_spent DESC
LIMIT 5;

SELECT p.product_id, p.product_name, SUM(oi.quantity) AS total_quantity
FROM Products p
JOIN Order_Items oi ON p.product_id = oi.product_id
GROUP BY p.product_id, p.product_name
ORDER BY total_quantity DESC
LIMIT 1;

SELECT c.customer_id, c.name
FROM Customers c
LEFT JOIN Orders o ON c.customer_id = o.customer_id
WHERE o.order_id IS NULL;

SELECT 
    DATE_FORMAT(order_date, '%Y-%m') AS month,
    SUM(total_amount) AS total_revenue
FROM Orders
GROUP BY DATE_FORMAT(order_date, '%Y-%m')
ORDER BY month;