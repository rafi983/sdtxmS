# Problem 9 - ON DELETE CASCADE
# Uses a separate demo database so online_course_db is not affected.

import mysql.connector

from db_config import DB_CONFIG

print("""
ON DELETE CASCADE means: when a parent row is deleted, all child rows
that reference it are automatically deleted by the database engine.

DDL with ON DELETE CASCADE:
  CREATE TABLE Course (
      CourseID     INT AUTO_INCREMENT PRIMARY KEY,
      Title        VARCHAR(255) NOT NULL,
      Credits      INT NOT NULL,
      InstructorID INT,
      FOREIGN KEY (InstructorID) REFERENCES Instructor(InstructorID)
          ON DELETE CASCADE
  );
""")

# Connect without a database to create the demo DB
cfg = {k: v for k, v in DB_CONFIG.items() if k != "database"}
conn = mysql.connector.connect(**cfg)
cursor = conn.cursor()

cursor.execute("DROP DATABASE IF EXISTS cascade_demo_db")
cursor.execute("CREATE DATABASE cascade_demo_db")
cursor.execute("USE cascade_demo_db")

cursor.execute("""
CREATE TABLE Instructor (
    InstructorID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL
)""")

cursor.execute("""
CREATE TABLE Course (
    CourseID     INT AUTO_INCREMENT PRIMARY KEY,
    Title        VARCHAR(255) NOT NULL,
    InstructorID INT,
    FOREIGN KEY (InstructorID) REFERENCES Instructor(InstructorID)
        ON DELETE CASCADE
)""")

cursor.executemany("INSERT INTO Instructor (Name) VALUES (%s)", [("Alice",), ("Bob",)])

cursor.executemany(
    "INSERT INTO Course (Title, InstructorID) VALUES (%s, %s)",
    [
        ("Python 101", 1),
        ("Data Structures", 1),
        ("Calculus I", 2),
        ("Linear Algebra", 2),
    ],
)

conn.commit()

# Show courses before delete
cursor.execute("SELECT CourseID, Title, InstructorID FROM Course")
print("Courses BEFORE deleting Instructor 1:")
for row in cursor.fetchall():
    print(" ", row)

# Delete instructor 1
cursor.execute("DELETE FROM Instructor WHERE InstructorID = 1")
conn.commit()
print("\nExecuted: DELETE FROM Instructor WHERE InstructorID = 1")

# Show courses after delete — only Bob's courses should remain
cursor.execute("SELECT CourseID, Title, InstructorID FROM Course")
print("\nCourses AFTER deleting Instructor 1 (Alice's courses were auto-deleted):")
for row in cursor.fetchall():
    print(" ", row)

# Cleanup
cursor.execute("DROP DATABASE cascade_demo_db")
conn.commit()
cursor.close()
conn.close()
print("\nDemo database dropped. online_course_db was not touched.")
