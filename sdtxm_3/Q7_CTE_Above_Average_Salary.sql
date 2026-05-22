-- Q7: CTE example - show employees whose salary is above average salary.

USE dummydb;

WITH avg_sal AS (
    SELECT AVG(salary) AS avg_salary
    FROM employees
)
SELECT e.first_name, e.last_name, e.salary
FROM employees e
JOIN avg_sal a
  ON e.salary > a.avg_salary
ORDER BY e.salary DESC;
