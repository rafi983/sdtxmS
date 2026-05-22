-- Q8: Display employees who earn less than Steven King.

USE dummydb;

SELECT e.first_name, e.last_name, e.salary
FROM employees e
WHERE e.salary < (
    SELECT salary
    FROM employees
    WHERE first_name = 'Steven' AND last_name = 'King'
)
ORDER BY e.salary DESC;
