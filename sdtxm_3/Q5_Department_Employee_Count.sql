-- Q5: Show department names and number of employees in each department.

USE dummydb;

SELECT d.department_name,
       COUNT(e.employee_id) AS employee_count
FROM departments d
LEFT JOIN employees e
  ON d.department_id = e.department_id
GROUP BY d.department_id, d.department_name
ORDER BY d.department_name;
