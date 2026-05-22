-- Q10: Display all city names where departments are located.

USE dummydb;

SELECT DISTINCT l.city
FROM departments d
JOIN locations l
  ON d.location_id = l.location_id
ORDER BY l.city;
