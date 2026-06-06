# Problem 4 - Find instructors who teach the most total credits

import mysql.connector

from db_config import DB_CONFIG

conn = mysql.connector.connect(**DB_CONFIG)
cursor = conn.cursor()

sql = """
SELECT i.Name, SUM(c.Credits) AS TotalCredits
FROM Instructor i
JOIN Course c ON i.InstructorID = c.InstructorID
GROUP BY i.InstructorID, i.Name
HAVING SUM(c.Credits) = (
    SELECT MAX(total) FROM (
        SELECT SUM(Credits) AS total
        FROM Course
        GROUP BY InstructorID
    ) AS sub
)
"""
print(f"SQL:\n{sql.strip()}\n")

cursor.execute(sql)
for row in cursor.fetchall():
    print(row)

cursor.close()
conn.close()
