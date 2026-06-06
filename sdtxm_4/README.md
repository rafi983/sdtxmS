# Online Course Management System — Python & MySQL Assignment

---

## Overview

This project is a Python + MySQL assignment that demonstrates core database
management concepts through a simulated **Online Course Management System**.
The system models instructors, students, courses, and enrolments. Each numbered
problem file (`problem_XX.py`) targets a specific SQL or database concept —
ranging from basic CRUD and aggregation to referential integrity, triggers,
stored procedures, and personal reflection.

---

## Prerequisites

| Requirement | Minimum Version |
|---|---|
| Python | 3.8+ |
| MySQL Server | 8.0+ |
| mysql-connector-python | 8.0+ |

---

## Installation

### 1. Clone or download the project

```bash
git clone <repository-url>
cd sdtxm_4
```

Or simply download and extract the ZIP, then open a terminal in the
`sdtxm_4` folder.

### 2. Install the Python driver

```bash
pip install mysql-connector-python
```

### 3. Configure `db_config.py`

Open `db_config.py` and update the connection details to match your MySQL
installation:

```python
DB_CONFIG = {
    "host":     "localhost",   # MySQL server host
    "user":     "root",        # MySQL username
    "password": "your_password",  # MySQL password  ← change this
    "database": "online_course_db",  # target database (created by setup_db.py)
}
```

> **Never commit real passwords.** Add `db_config.py` to `.gitignore` if you
> push this project to a public repository.

---

## Database Setup

Run the setup script **once** before executing any problem file:

```bash
python setup_db.py
```

This script:
- Creates the `online_course_db` database if it does not already exist.
- Creates the four core tables (see [Schema Diagram](#schema-diagram) below).
- Populates each table with sample data.

### Tables created

| Table | Rows inserted | Description |
|---|---|---|
| `Instructor` | 4 | Faculty members who teach courses |
| `Student` | 6 | Registered students |
| `Course` | 5 | Courses offered, each linked to an instructor |
| `Enrollment` | 14 | Student–course registrations with dates |

---

## Project Structure

```
sdtxm_4/
│
├── db_config.py          # Shared DB connection settings (edit before running)
├── setup_db.py           # Creates online_course_db schema and sample data
│
├── problem_01.py         # ER diagram — Online Course Management System
├── problem_02.py         # INSERT enrollment for StudentID=5 into highest-credit course
├── problem_03.py         # UPDATE — assign a new instructor to CourseID=3
├── problem_04.py         # SELECT — find instructors who teach the most total credits
├── problem_05.py         # SELECT — list students enrolled in more than two courses
├── problem_06.py         # ER diagram — Simple Online Retail System + DDL
├── problem_07.py         # GROUP BY vs ORDER BY explanation with live demos
├── problem_08.py         # Second-highest salary (3 methods)
├── problem_09.py         # ON DELETE CASCADE referential integrity demo
├── problem_10.py         # Personal reflection essay (no DB required)
│
└── README.md             # This file
```

---

## Problems at a Glance

| File | # | Topic | Key SQL / Concept |
|---|---|---|---|
| `problem_01.py` | 1 | ER Diagram — Course System | Entity-Relationship design, no DB |
| `problem_02.py` | 2 | Insert into max-credit course | `INSERT`, subquery, `ORDER BY … LIMIT 1` |
| `problem_03.py` | 3 | Update course instructor | `UPDATE … SET … WHERE` |
| `problem_04.py` | 4 | Instructors with most credits | `GROUP BY`, `SUM`, `HAVING`, correlated subquery |
| `problem_05.py` | 5 | Students in > 2 courses | `JOIN`, `GROUP BY`, `HAVING COUNT > 2` |
| `problem_06.py` | 6 | ER Diagram — Retail System | Entity-Relationship design + DDL, no DB |
| `problem_07.py` | 7 | GROUP BY vs ORDER BY | Comparison, live demo, `HAVING` |
| `problem_08.py` | 8 | Second-highest salary | Subquery, `LIMIT/OFFSET`, `DENSE_RANK()` |
| `problem_09.py` | 9 | ON DELETE CASCADE | FK referential actions, isolation demo |
| `problem_10.py` | 10 | Personal Reflection | Essay — no DB needed |

---

## Running Each Problem

Make sure you have run `python setup_db.py` first (Problems 2–5, 7–9 need the DB).

```bash
# Problem 1 — Prints the ER diagram for the Online Course Management System (no DB)
python problem_01.py

# Problem 2 — Inserts an enrollment for StudentID=5 into the highest-credit course
python problem_02.py

# Problem 3 — Updates CourseID=3 to a new instructor; shows before/after
python problem_03.py

# Problem 4 — Finds the instructor(s) with the highest total credited hours
python problem_04.py

# Problem 5 — Lists every student enrolled in more than 2 courses
python problem_05.py

# Problem 6 — Prints the ER diagram for a retail system plus CREATE TABLE DDL (no DB)
python problem_06.py

# Problem 7 — Explains GROUP BY vs ORDER BY then runs 3 live demos
python problem_07.py

# Problem 8 — Finds the second-highest instructor salary using 3 different methods
python problem_08.py

# Problem 9 — Creates a temporary cascade_demo_db, proves ON DELETE CASCADE,
#             then drops the demo database (online_course_db is unaffected)
python problem_09.py

# Problem 10 — Prints a personal reflection essay; requires no database
python problem_10.py
```

---

## Schema Diagram

```
┌─────────────────────────┐          ┌──────────────────────────────┐
│        Instructor        │          │            Course             │
├─────────────────────────┤          ├──────────────────────────────┤
│ InstructorID  INT  PK   │◄────┐    │ CourseID     INT  PK         │
│ Name          VARCHAR   │     │    │ Title        VARCHAR          │
│ Email         VARCHAR   │     │    │ Credits      INT              │
│ Phone         VARCHAR   │     └────│ InstructorID INT  FK         │
│ Department    VARCHAR   │          │              (ON DELETE CASCADE)│
│ Salary        DECIMAL   │          └──────────────────────────────┘
└─────────────────────────┘                        │
                                                   │
┌─────────────────────────┐          ┌──────────────────────────────┐
│         Student          │          │          Enrollment           │
├─────────────────────────┤          ├──────────────────────────────┤
│ StudentID     INT  PK   │◄────┐    │ EnrollmentID INT  PK         │
│ Name          VARCHAR   │     └────│ StudentID    INT  FK         │
│ Email         VARCHAR   │          │ CourseID     INT  FK ────────►│
│ Phone         VARCHAR   │          │ EnrollmentDate DATE          │
└─────────────────────────┘          └──────────────────────────────┘
```

**Relationships:**
- One `Instructor` teaches zero or more `Course`s (`1 : N`).
- One `Student` has zero or more `Enrollment`s (`1 : N`).
- One `Course` has zero or more `Enrollment`s (`1 : N`).
- `Enrollment` is the junction that associates `Student` ↔ `Course` (`M : N`).

---

## Sample Data

### Instructors

| InstructorID | Name | Department | Salary |
|---|---|---|---|
| 1 | Dr. Alice | CS | 90,000 |
| 2 | Dr. Bob | Math | 85,000 |
| 3 | Dr. Carol | Physics | 90,000 |
| 4 | Dr. Dave | CS | 75,000 |

### Students

| StudentID | Name | Email |
|---|---|---|
| 1 | Alice | alice@student.edu |
| 2 | Bob | bob@student.edu |
| 3 | Carol | carol@student.edu |
| 4 | Dave | dave@student.edu |
| 5 | Eve | eve@student.edu |
| 6 | Frank | frank@student.edu |

### Courses

| CourseID | Title | Credits | InstructorID |
|---|---|---|---|
| 1 | Python Programming | 3 | 1 |
| 2 | Calculus I | 4 | 2 |
| 3 | Quantum Mechanics | 4 | 3 |
| 4 | Data Structures | 2 | 4 |
| 5 | Machine Learning | 5 | 1 |

> **Note:** Eve (StudentID=5) is deliberately **not** enrolled in Machine Learning (CourseID=5, Credits=5) in the seed data — `problem_02.py` inserts that enrollment as its demonstration.

---

## Notes

- **`problem_09.py`** creates a completely separate database called
  `cascade_demo_db` for its demonstration. This database is automatically
  dropped at the end of the script. **`online_course_db` is never modified
  by Problem 9.**

- **`problem_10.py`** is a standalone script that prints a personal reflection
  essay to the console. It does **not** import `db_config.py` or open any
  database connection — it can be run without MySQL being available.

- All other problem files read from (and in some cases temporarily modify)
  `online_course_db`. Any modifications made by individual problems are
  intended as demonstrations and are either rolled back or cleaned up within
  the same script.

- If you encounter an `Access denied` error, verify that the MySQL user
  specified in `db_config.py` has the necessary privileges:

  ```sql
  GRANT ALL PRIVILEGES ON online_course_db.* TO 'root'@'localhost';
  GRANT CREATE, DROP ON *.* TO 'root'@'localhost';  -- needed by problem_09
  FLUSH PRIVILEGES;
  ```

---

## License

This project is released under the [MIT License](https://opensource.org/licenses/MIT).

```
MIT License

Copyright (c) 2024

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
