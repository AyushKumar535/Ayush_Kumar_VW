CREATE DATABASE employee_db;
USE employee_db;

CREATE TABLE Employees (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50),
    department VARCHAR(50),
    salary DECIMAL(10,2)
);

INSERT INTO Employees (emp_id, emp_name, department, salary) VALUES
(1, 'Alice', 'HR', 5000.00),
(2, 'Bob', 'IT', 7000.00),
(3, 'Charlie', 'IT', 6000.00),
(4, 'David', 'Finance', 8000.00),
(5, 'Eve', 'Finance', 7500.00),
(6, 'Frank', 'HR', 4500.00),
(7, 'Ayush', 'IT', 9000.00),
(8, 'Hannah', 'Finance', 8200.00);

SELECT emp_id, emp_name, department, salary
FROM Employees
WHERE salary > (SELECT AVG(salary) FROM Employees);

SELECT emp_id, emp_name, department, salary
FROM Employees e
WHERE salary > (
    SELECT AVG(salary)
    FROM Employees
    WHERE department = e.department
);

SELECT emp_id, emp_name, department, salary
FROM Employees e
WHERE salary = (
    SELECT MAX(salary)
    FROM Employees
    WHERE department = e.department
);

SELECT emp_id, emp_name, department, salary
FROM Employees
WHERE salary > (SELECT AVG(salary) FROM Employees)
  AND salary < (SELECT MAX(salary) FROM Employees);
  
SELECT department, AVG(salary) AS avg_dept_salary
FROM Employees
GROUP BY department
HAVING AVG(salary) > (SELECT AVG(salary) FROM Employees);
    
