# Problem 7 - GROUP BY vs ORDER BY

import mysql.connector

from db_config import DB_CONFIG

print("""
GROUP BY vs ORDER BY
====================

ORDER BY  - Sorts the result rows. Does NOT reduce the number of rows.
            Used to control the display order of output.

GROUP BY  - Groups rows that share a value into summary rows.
            Used with aggregate functions (COUNT, SUM, AVG, etc.).
            Reduces many rows into one row per group.

Key difference:
  ORDER BY  → changes the ORDER of rows
  GROUP BY  → changes the NUMBER of rows (collapses them into groups)
""")

conn = mysql.connector.connect(**DB_CONFIG)
cursor = conn.cursor()

# ORDER BY example
print("--- ORDER BY example: list all courses sorted by Credits ---")
sql_order = "SELECT Title, Credits FROM Course ORDER BY Credits DESC"
print(f"SQL: {sql_order}\n")
cursor.execute(sql_order)
for row in cursor.fetchall():
    print(row)

# GROUP BY example
print("\n--- GROUP BY example: count courses per instructor ---")
sql_group = """
SELECT i.Name, COUNT(c.CourseID) AS NumCourses
FROM Instructor i
JOIN Course c ON i.InstructorID = c.InstructorID
GROUP BY i.InstructorID, i.Name
"""
print(f"SQL: {sql_group.strip()}\n")
cursor.execute(sql_group)
for row in cursor.fetchall():
    print(row)

cursor.close()
conn.close()
