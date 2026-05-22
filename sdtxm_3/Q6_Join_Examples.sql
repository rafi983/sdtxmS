-- Q6: INNER JOIN, LEFT JOIN, RIGHT JOIN, and CROSS JOIN examples.

USE dummydb;

-- INNER JOIN: only matching rows
SELECT e.first_name, d.department_name
FROM employees e
INNER JOIN departments d
  ON e.department_id = d.department_id;

-- LEFT JOIN: all employees + matching departments
SELECT e.first_name, d.department_name
FROM employees e
LEFT JOIN departments d
  ON e.department_id = d.department_id;

-- RIGHT JOIN: all departments + matching employees
SELECT e.first_name, d.department_name
FROM employees e
RIGHT JOIN departments d
  ON e.department_id = d.department_id;

-- CROSS JOIN: Cartesian product
SELECT e.first_name, d.department_name
FROM employees e
CROSS JOIN departments d;
