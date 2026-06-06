# Problem 10 - Personal Reflection: Most Challenging Topic
# No database connection needed.

print("""
Most Challenging Topic in This Course
======================================

The most challenging topic I encountered was SQL JOINs and subqueries.

Why it was challenging:
  At first, it was hard to visualise how two or more tables are combined
  into a single result set. The different JOIN types (INNER, LEFT, RIGHT)
  each produce different row counts, and understanding when NULLs appear
  in a LEFT JOIN versus an INNER JOIN took repeated practice. Correlated
  subqueries were even harder because the inner query runs once per row
  of the outer query, making it difficult to trace the logic mentally.

  Another source of confusion was knowing when to use a subquery versus
  a JOIN — both can often solve the same problem, but they perform
  differently depending on the data size and indexes available.

How I overcame it:
  I started by drawing the tables on paper and manually tracing which
  rows would match before writing any SQL. Breaking queries into smaller
  steps helped: first write the JOIN to see the raw combined rows, then
  add the WHERE or GROUP BY clause. Using MySQL Workbench's visual
  EXPLAIN output also helped me understand query execution order.
  Practicing on the course schema with real data made the results
  concrete and easier to verify.

Key takeaway:
  JOINs and subqueries are the foundation of meaningful SQL. Once the
  mental model of "matching rows across tables" clicks, everything else
  — aggregation, filtering, ranking — becomes much more straightforward.
""")
