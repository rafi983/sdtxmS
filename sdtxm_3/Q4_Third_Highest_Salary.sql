-- Q4: Using dummydb, get the third-highest distinct salary in employees.

USE dummydb;

SELECT salary AS third_highest_salary
FROM (
    SELECT DISTINCT salary
    FROM employees
    ORDER BY salary DESC
    LIMIT 1 OFFSET 2
) t;
