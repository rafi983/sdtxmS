import mysql.connector

from db_config import DB_CONFIG

# Connect without selecting a database to create it first
cfg = {k: v for k, v in DB_CONFIG.items() if k != "database"}
conn = mysql.connector.connect(**cfg)
cursor = conn.cursor()

cursor.execute("DROP DATABASE IF EXISTS online_course_db")
cursor.execute("CREATE DATABASE online_course_db")
cursor.execute("USE online_course_db")

cursor.execute("""
CREATE TABLE Instructor (
    InstructorID INT AUTO_INCREMENT PRIMARY KEY,
    Name         VARCHAR(255) NOT NULL,
    Email        VARCHAR(255) NOT NULL UNIQUE,
    Phone        VARCHAR(15),
    Department   VARCHAR(50),
    Salary       DECIMAL(10,2)
)""")

cursor.execute("""
CREATE TABLE Student (
    StudentID INT AUTO_INCREMENT PRIMARY KEY,
    Name      VARCHAR(255) NOT NULL,
    Email     VARCHAR(255) NOT NULL UNIQUE,
    Phone     VARCHAR(15)
)""")

cursor.execute("""
CREATE TABLE Course (
    CourseID     INT AUTO_INCREMENT PRIMARY KEY,
    Title        VARCHAR(255) NOT NULL,
    Credits      INT NOT NULL,
    InstructorID INT,
    FOREIGN KEY (InstructorID) REFERENCES Instructor(InstructorID)
)""")

cursor.execute("""
CREATE TABLE Enrollment (
    EnrollmentID   INT AUTO_INCREMENT PRIMARY KEY,
    StudentID      INT,
    CourseID       INT,
    EnrollmentDate DATE NOT NULL,
    FOREIGN KEY (StudentID) REFERENCES Student(StudentID),
    FOREIGN KEY (CourseID)  REFERENCES Course(CourseID)
)""")

cursor.executemany(
    "INSERT INTO Instructor (Name, Email, Phone, Department, Salary) VALUES (%s,%s,%s,%s,%s)",
    [
        ("Dr. Alice", "alice@uni.edu", "555-0101", "CS", 90000),
        ("Dr. Bob", "bob@uni.edu", "555-0102", "Math", 85000),
        ("Dr. Carol", "carol@uni.edu", "555-0103", "Physics", 90000),
        ("Dr. Dave", "dave@uni.edu", "555-0104", "CS", 75000),
    ],
)

cursor.executemany(
    "INSERT INTO Student (Name, Email, Phone) VALUES (%s,%s,%s)",
    [
        ("Alice", "alice@student.edu", "555-1001"),
        ("Bob", "bob@student.edu", "555-1002"),
        ("Carol", "carol@student.edu", "555-1003"),
        ("Dave", "dave@student.edu", "555-1004"),
        ("Eve", "eve@student.edu", "555-1005"),  # StudentID=5
        ("Frank", "frank@student.edu", "555-1006"),
    ],
)

cursor.executemany(
    "INSERT INTO Course (Title, Credits, InstructorID) VALUES (%s,%s,%s)",
    [
        ("Python Programming", 3, 1),
        ("Calculus I", 4, 2),
        ("Quantum Mechanics", 4, 3),
        ("Data Structures", 2, 4),
        ("Machine Learning", 5, 1),  # CourseID=5, highest credits
    ],
)

# Alice(1), Bob(2), Carol(3) each in 3 courses  →  satisfies Problem 5
# Eve(5) is NOT enrolled in Machine Learning(5)  →  Problem 2 inserts it
cursor.executemany(
    "INSERT INTO Enrollment (StudentID, CourseID, EnrollmentDate) VALUES (%s,%s,%s)",
    [
        (1, 1, "2024-01-15"),
        (1, 2, "2024-01-15"),
        (1, 3, "2024-01-16"),
        (2, 1, "2024-01-15"),
        (2, 2, "2024-01-16"),
        (2, 4, "2024-01-17"),
        (3, 2, "2024-01-15"),
        (3, 3, "2024-01-16"),
        (3, 4, "2024-01-17"),
        (4, 3, "2024-01-15"),
        (4, 5, "2024-01-18"),
        (5, 1, "2024-01-15"),
        (5, 4, "2024-01-17"),
        (6, 5, "2024-01-18"),
    ],
)

conn.commit()
cursor.close()
conn.close()
print("Database setup complete.")
