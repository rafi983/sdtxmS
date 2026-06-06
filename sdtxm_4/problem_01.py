# Problem 1 - ER Diagram: Online Course Management System
# No database connection needed.

print("""
ER DIAGRAM - Online Course Management System
============================================

  +------------------+          +------------------+
  |    INSTRUCTOR    |          |     STUDENT      |
  +------------------+          +------------------+
  | *InstructorID    |          | *StudentID       |
  |  Name            |          |  Name            |
  |  Email           |          |  Email           |
  |  Phone           |          |  Phone           |
  |  Department      |          +--------+---------+
  +--------+---------+                   |
           | 1                           | 1
           |                             |
           | N                           | N
  +--------+---------+          +--------+---------+
  |      COURSE      |          |    ENROLLMENT    |
  +------------------+          +------------------+
  | *CourseID        | 1      N | *EnrollmentID    |
  |  Title           +----------+ #StudentID       |
  |  Credits         |          | #CourseID        |
  | #InstructorID    |          |  EnrollmentDate  |
  +------------------+          +------------------+

Legend:  * = Primary Key    # = Foreign Key

Relationships:
  - One INSTRUCTOR teaches many COURSEs         (1:N)
  - One STUDENT has many ENROLLMENTs            (1:N)
  - One COURSE appears in many ENROLLMENTs      (1:N)
  - STUDENT and COURSE have a M:N relationship
    resolved through the ENROLLMENT junction table
""")
