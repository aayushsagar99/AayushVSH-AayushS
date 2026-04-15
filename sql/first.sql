DROP TABLE IF EXISTS employees;

-- This script creates a simple "Employees" table and performs common tasks.

-- 1. Create a table to store employee info
CREATE TABLE employees (
    id INTEGER PRIMARY KEY,
    name TEXT,
    department TEXT,
    salary INTEGER,
    hire_date DATE
);

-- 2. Add some sample data (Insert)
INSERT INTO employees (id, name, department, salary, hire_date)
VALUES 
    (1, 'Alice Smith', 'Engineering', 95000, '2022-03-15'),
    (2, 'Bob Jones', 'Marketing', 72000, '2021-11-01'),
    (3, 'Charlie Brown', 'Engineering', 88000, '2023-01-10'),
    (4, 'Diana Prince', 'Sales', 65000, '2020-05-20');

-- 3. Find all Engineering employees making over 80k (Select & Filter)
SELECT name, salary 
FROM employees 
WHERE department = 'Engineering' 
  AND salary > 80000;

-- 4. Calculate the average salary by department (Aggregate)
SELECT department, AVG(salary) AS average_pay
FROM employees
GROUP BY department;

-- 5. Give everyone in Sales a 10% raise (Update)
UPDATE employees 
SET salary = salary * 1.10 
WHERE department = 'Sales';

-- This removes Bob from the table
DELETE FROM employees WHERE name = 'Bob Jones';

-- This shows everyone who is left
SELECT * FROM employees;
