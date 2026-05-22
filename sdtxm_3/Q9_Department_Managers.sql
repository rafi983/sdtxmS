-- Q9: Find department names and manager names for each department.

USE dummydb;

SELECT d.department_name,
       CONCAT(m.first_name, ' ', m.last_name) AS manager_name
FROM departments d
LEFT JOIN employees m
  ON d.manager_id = m.employee_id
ORDER BY d.department_name;
