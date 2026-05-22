# SQL Assignment Solutions (Final 10 Files)

This folder now follows a clean **Q1 to Q10** structure, as requested.

## Final file mapping

### Q1
- **File:** `Q1_PrimaryKey_vs_ForeignKey.sql`
- **Covers:** Difference between Primary Key and Foreign Key

### Q2
- **File:** `Q2_SelfJoin_Employees.sql`
- **Covers:** Self Join example on `employees` for same `manager_id`

### Q3
- **File:** `Q3_Create_Tables.sql`
- **Covers (combined):**
  - Create `Employees`
  - Create `Projects`
  - Create `Employee_Projects` (many-to-many)

### Q4
- **File:** `Q4_Third_Highest_Salary.sql`
- **Covers:** Third-highest salary in `employees`

### Q5
- **File:** `Q5_Department_Employee_Count.sql`
- **Covers:** Department names with employee counts

### Q6
- **File:** `Q6_Join_Examples.sql`
- **Covers:** INNER, LEFT, RIGHT, CROSS JOIN examples

### Q7
- **File:** `Q7_CTE_Above_Average_Salary.sql`
- **Covers:** CTE example (employees above average salary)

### Q8
- **File:** `Q8_Less_Than_Steven_King.sql`
- **Covers:** Employees with salary lower than Steven King

### Q9
- **File:** `Q9_Department_Managers.sql`
- **Covers:** Department names with manager names

### Q10
- **File:** `Q10_Department_Cities.sql`
- **Covers:** Cities where departments are located

---

## Run order

1. Run `00 DUMMY_DATABASE.sql` to create and populate `dummydb`.
2. Run `Q1` to `Q10` as needed.

---

## Notes

- Files that query the sample schema include `USE dummydb;`.
