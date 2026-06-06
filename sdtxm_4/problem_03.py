# Problem 3 - UPDATE: Assign a new instructor to CourseID=3

import mysql.connector

from db_config import DB_CONFIG

conn = mysql.connector.connect(**DB_CONFIG)
cursor = conn.cursor()

# Show current state
cursor.execute("SELECT CourseID, Title, InstructorID FROM Course WHERE CourseID = 3")
print("Before:", cursor.fetchone())

# Update InstructorID to 2
sql = "UPDATE Course SET InstructorID = 2 WHERE CourseID = 3"
print(f"\nSQL:\n{sql}")

cursor.execute(sql)
conn.commit()
print(f"\nRows affected: {cursor.rowcount}")

# Show updated state
cursor.execute("""
    SELECT c.CourseID, c.Title, c.InstructorID, i.Name AS InstructorName
    FROM Course c
    JOIN Instructor i ON c.InstructorID = i.InstructorID
    WHERE c.CourseID = 3
""")
print("After:", cursor.fetchone())

cursor.close()
conn.close()
