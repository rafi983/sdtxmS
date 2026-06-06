# Problem 8 - Find the second-highest salary among instructors

import mysql.connector

from db_config import DB_CONFIG

conn = mysql.connector.connect(**DB_CONFIG)
cursor = conn.cursor()

sql = """
SELECT MAX(Salary) AS SecondHighestSalary
FROM Instructor
WHERE Salary < (SELECT MAX(Salary) FROM Instructor)
"""
print(f"SQL:\n{sql.strip()}\n")

cursor.execute(sql)
print("Second Highest Salary:", cursor.fetchone()[0])

cursor.close()
conn.close()
