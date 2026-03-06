CREATE DATABASE CompanyDB;
USE CompanyDB;
CREATE TABLE Employees (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50),
    department VARCHAR(50),
    salary DECIMAL(10,2),
    joining_date DATE
);
CREATE TABLE Projects (
    project_id INT PRIMARY KEY,
    project_name VARCHAR(50),
    start_date DATE,
    end_date DATE
);
CREATE TABLE Employee_Project (
    emp_id INT,
    project_id INT,
    hours_worked INT,
    rating DECIMAL(2,1),
    PRIMARY KEY (emp_id, project_id),
    FOREIGN KEY (emp_id) REFERENCES Employees(emp_id),
    FOREIGN KEY (project_id) REFERENCES Projects(project_id)
);

INSERT INTO Employees (emp_id, emp_name, department, salary, joining_date)
VALUES
(1, 'Alice', 'IT', 70000, '2021-01-15'),
(2, 'Bob', 'Finance', 80000, '2020-05-10'),
(3, 'Charlie', 'IT', 90000, '2019-07-20'),
(4, 'David', 'HR', 60000, '2022-03-05'),
(5, 'Eve', 'Finance', 75000, '2021-11-30');

INSERT INTO Projects (project_id, project_name, start_date, end_date)
VALUES
(101, 'Project Alpha', '2023-01-01', '2023-06-30'),
(102, 'Project Beta', '2023-02-15', '2023-07-15'),
(103, 'Project Gamma', '2023-03-01', '2023-09-30'),
(104, 'Project Delta', '2023-04-01', '2023-10-01');

INSERT INTO Employee_Project (emp_id, project_id, hours_worked, rating)
VALUES
(1, 101, 120, 5),
(1, 102, 80, 4),
(2, 101, 100, 3),
(2, 103, 90, 5),
(3, 101, 150, 4),
(3, 102, 110, 5),
(3, 103, 120, 4),
(4, 104, 70, 3);


SELECT e.emp_id, e.emp_name, COUNT(ep.project_id) AS project_count
FROM Employees e
JOIN Employee_Project ep ON e.emp_id = ep.emp_id
GROUP BY e.emp_id, e.emp_name
HAVING COUNT(ep.project_id) > 2;   

SELECT e.emp_id, e.emp_name, AVG(ep.rating) AS avg_rating
FROM Employees e
JOIN Employee_Project ep ON e.emp_id = ep.emp_id
GROUP BY e.emp_id, e.emp_name
HAVING AVG(ep.rating) > 4;

SELECT e.department, e.emp_id, e.emp_name, e.salary
FROM Employees e
JOIN (
    SELECT department, MAX(salary) AS max_salary
    FROM Employees
    GROUP BY department
) dept_max ON e.department = dept_max.department AND e.salary = dept_max.max_salary;

SELECT e.emp_id, e.emp_name
FROM Employees e
LEFT JOIN Employee_Project ep ON e.emp_id = ep.emp_id
WHERE ep.emp_id IS NULL;

SELECT p.project_id, p.project_name, SUM(ep.hours_worked) AS total_hours
FROM Projects p
JOIN Employee_Project ep ON p.project_id = ep.project_id
GROUP BY p.project_id, p.project_name
ORDER BY total_hours DESC
LIMIT 1;