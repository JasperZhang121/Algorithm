# Precedence:
SQL statements are executed in a specific order based on their precedence, which is determined by the SQL standard. Here is a general order of precedence for SQL statements:
​
- FROM clause: This is where the data is retrieved from.
- WHERE clause: This is where filtering is applied to the data retrieved from the FROM - clause.
- GROUP BY clause: This is where the data is grouped into sets.
- HAVING clause: This is where filtering is applied to the grouped data.
- SELECT clause: This is where the columns to be returned are specified.
- ORDER BY clause: This is where the data is sorted.
- LIMIT/OFFSET clauses: These are used to limit the number of rows returned by the query.
​
​
​
---
​
In this question:
- The inner query (SELECT MAX(salary) FROM Employee) returns the highest salary in the table.
- The outer query selects the maximum salary that is less than the highest salary. This gives us the second highest salary.
- If there is no second highest salary (i.e., if the table has less than two distinct salary values), the query will return null.
​