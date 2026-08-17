CREATE TABLE Employee(
emp_id SERIAL PRIMARY KEY,
emp_name VARCHAR(20) NOT NULL,
dept VARCHAR(20) CHECK (dept in ('FINANCE','SALES','ENGINEERS')),
salary FLOAT NOT NULL
);

CREATE TABLE Department_heads(
dept VARCHAR(20) PRIMARY KEY CHECK (dept in ('FINANCE','SALES','ENGINEERS')), -- foreign key
HOD VARCHAR(20) NOT NULL
);

INSERT INTO Employee (emp_name, dept, salary) VALUES
('Srishti', 'FINANCE', 45000),
('Vian', 'SALES', 55000),
('Alan', 'ENGINEERS', 65000),
('Rashmi', 'FINANCE', 50000),
('Karthik', 'ENGINEERS', 75000),
('Meera', 'SALES', 40000),
('Aditya', 'ENGINEERS', 85000),
('Nithya', 'FINANCE', 60000),
('Rohan', 'SALES', 35000),
('Ananya', 'ENGINEERS', 70000),
('Devika', 'FINANCE', 90000),
('Arjun', 'SALES', 50000);

SELECT * 
FROM Employee;

SELECT DISTINCT dept
FROM Employee;

SELECT * 
FROM Employee
WHERE salary > 50000;

SELECT *
FROM Employee
WHERE dept = 'FINANCE';

SELECT *
FROM Employee
WHERE salary BETWEEN 
40000 TO 70000;

SELECT *
FROM Employee
WHERE dept IN('SALES', 'ENGINEERS');

SELECT *
FROM Employee
ORDER BY salary desc;

