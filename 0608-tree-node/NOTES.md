# When
In SQL, the "WHEN" statement is typically used in conjunction with the "CASE" statement to specify conditions that determine the output of the query. The syntax for the "CASE" statement with the "WHEN" clause is as follows:

```sql
CASE 
  WHEN condition1 THEN result1
  WHEN condition2 THEN result2
  ...
  ELSE resultN
END
```

In SQL, the "WHEN" statement is typically used in conjunction with the "CASE" statement to specify conditions that determine the output of the query. The syntax for the "CASE" statement with the "WHEN" clause is as follows:

Here, "condition1", "condition2", etc. are expressions that evaluate to true or false. If a condition is true, the corresponding "result" is returned. If none of the conditions are true, the "ELSE" result (resultN) is returned.

---

In this quesion:

- use when statement to identify the type
- if null then root, if in both id then inner, others are leaf
- rename it as type


