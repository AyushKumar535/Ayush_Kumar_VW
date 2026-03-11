Create database company_vw;
use company_vw;

CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(100) NOT NULL,
    password VARCHAR(100) NOT NULL,
    role VARCHAR(20) NOT NULL
);

CREATE TABLE employees (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    email VARCHAR(100),
    department VARCHAR(100),
    manager_id INT
);

INSERT INTO users (username, password, role) VALUES
('admin', '123', 'admin'),
('manager1', '123', 'manager'),
('employee1', '123', 'employee');

select * from users;

INSERT INTO employees (name, email, department, manager_id) VALUES
('Admin User', 'admin@company.com', 'Management', NULL),
('Manager User', 'manager@company.com', 'IT', 1),
('Employee User', 'employee@company.com', 'IT', 2),
('Abhinav', 'abhi@pn.com','Management',2);

select * from employees;