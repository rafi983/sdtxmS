-- Q2: Self Join example using employees table.
-- List employee first names who share the same manager_id.

SELECT e1.first_name AS employee_1,
       e2.first_name AS employee_2,
       e1.manager_id
FROM employees e1
JOIN employees e2
  ON e1.manager_id = e2.manager_id
 AND e1.employee_id < e2.employee_id
WHERE e1.manager_id IS NOT NULL
ORDER BY e1.manager_id, e1.first_name, e2.first_name;
