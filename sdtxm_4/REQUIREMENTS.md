This schema represents a basic Online Course Management System. Answer questions 1 - 5 based on this schema.

CREATE TABLE Instructor (	
    InstructorID INT AUTO_INCREMENT PRIMARY KEY,	
    Name VARCHAR(255) NOT NULL,	
    Email VARCHAR(255) NOT NULL UNIQUE,	
    Phone VARCHAR(15),	
    Department VARCHAR(50)	
);	

CREATE TABLE Course (	
    CourseID INT AUTO_INCREMENT PRIMARY KEY,	
    Title VARCHAR(255) NOT NULL,	
    Credits INT NOT NULL,	
    InstructorID INT,	
    FOREIGN KEY (InstructorID) REFERENCES Instructor(InstructorID)	
);	

CREATE TABLE Enrollment (	
    EnrollmentID INT AUTO_INCREMENT PRIMARY KEY,	
    StudentID INT,	
    CourseID INT,	
    EnrollmentDate DATE NOT NULL,	
    FOREIGN KEY (StudentID) REFERENCES Student(StudentID),	
    FOREIGN KEY (CourseID) REFERENCES Course(CourseID)	
);	

CREATE TABLE Student (	
    StudentID INT AUTO_INCREMENT PRIMARY KEY,	
    Name VARCHAR(255) NOT NULL,	
    Email VARCHAR(255) NOT NULL UNIQUE,	
    Phone VARCHAR(15)	
);


    
QUESTIONS
Marks
1
Draw an Entity-Relationship (ER) diagram to represent this Online Course Management System schema.
10
2
Write an SQL query to insert a new enrollment record for a student (e.g., StudentID 5) into the course with the highest credit hours.
10
3
Write an SQL UPDATE query to assign a new instructor to a course (e.g., CourseID 3) by updating the InstructorID.
10
4
Write an SQL query to find the names of instructors who teach the most credits (total).
10
5
Write an SQL query to list all students who are enrolled in more than two courses.
10
6
Design an ER diagram for a simple online retail system that includes entities such as Customers, Products, and Orders. Keep the diagram simple.
10
7
Explain the difference between GROUP BY and ORDER BY in SQL. Provide an example for each to illustrate.
10
8
Given a table Instructor with a Salary column, write an SQL query to find the second-highest salary among instructors.
10
9
You have two tables, Instructor and Course. Use ON DELETE CASCADE on Course so that all courses are deleted when an instructor is removed.
10
10
Describe the most challenging topic you encountered in this course. Explain why it was challenging and how you overcame it.
10
