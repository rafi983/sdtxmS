# Problem 2 - Insert enrollment for StudentID=5 into the course with the highest credits

import mysql.connector

from db_config import DB_CONFIG

conn = mysql.connector.connect(**DB_CONFIG)
cursor = conn.cursor()

# Find the course with the highest credits
cursor.execute("""
    SELECT CourseID, Title, Credits
    FROM Course
    ORDER BY Credits DESC
    LIMIT 1
""")
course = cursor.fetchone()
course_id, title, credits = course
print(
    f"Course with highest credits: CourseID={course_id}, Title='{title}', Credits={credits}"
)

# Insert the enrollment
sql = """
    INSERT INTO Enrollment (StudentID, CourseID, EnrollmentDate)
    VALUES (5, %s, CURDATE())
"""
print(f"\nSQL:\n{sql.strip()}")

cursor.execute(sql, (course_id,))
conn.commit()
print(f"\nInserted enrollment: StudentID=5 into CourseID={course_id}")

cursor.close()
conn.close()
