# Problem 5 - List all students enrolled in more than two courses

import mysql.connector

from db_config import DB_CONFIG

conn = mysql.connector.connect(**DB_CONFIG)
cursor = conn.cursor()

sql = """
SELECT s.StudentID, s.Name, COUNT(e.CourseID) AS CourseCount
FROM Student s
JOIN Enrollment e ON s.StudentID = e.StudentID
GROUP BY s.StudentID, s.Name
HAVING COUNT(e.CourseID) > 2
"""
print(f"SQL:\n{sql.strip()}\n")

cursor.execute(sql)
for row in cursor.fetchall():
    print(row)

cursor.close()
conn.close()
