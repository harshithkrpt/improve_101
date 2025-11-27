Here comes a buffet of 50+ MySQL practice questions — pure questions only, neatly grouped by **DDL**, **DML**, **DQL**, **TCL**, **Joins**, **Subqueries**, and **Misc**. Perfect for drilling your SQL muscles.

---

# **MySQL Practice Questions (Copy-Friendly Markdown)**

## **DDL (Data Definition Language)**

1. Create a table `employees` with id, name, salary, and department.
2. Alter a table to add a new column `created_at` with default current timestamp.
3. Alter a column datatype from INT to BIGINT.
4. Drop a column from a table.
5. Rename a table from `orders` to `customer_orders`.
6. Create a table with a foreign key referencing another table.
7. Create a composite primary key on two columns.
8. Add a UNIQUE constraint to the `email` column.
9. Remove a primary key from a table.
10. Change a column name in a table.
11. Create an index on `last_name` column.
12. Create a full-text index on a `description` column.
13. Drop an index from a table.
14. Create a table using `CHECK` constraint (MySQL 8+).
15. Create a view named `active_users` that filters only active users.

---

## **DML (Data Manipulation Language)**

16. Insert a new row into the `employees` table.
17. Insert multiple rows in a single insert query.
18. Update salary of all employees in "HR" department by 10%.
19. Delete all employees with salary below 30000.
20. Insert a row only if email is not already present.
21. Update a row using a JOIN with another table.
22. Delete records from one table using a subquery.
23. Insert into a table selecting data from another table.
24. Replace a row if duplicate primary key is inserted.
25. Use `ON DUPLICATE KEY UPDATE` while inserting.

---

## **DQL (Data Query Language — SELECT)**

26. Select all columns from a table.
27. Select only distinct cities from a table.
28. Order results by salary descending.
29. Get the top 5 highest paid employees.
30. Count total rows in a table.
31. Count distinct values of a column.
32. Get the average salary of each department.
33. Group employees by department and sum salaries.
34. Retrieve rows where name starts with ‘A’.
35. Retrieve rows where email ends with ‘gmail.com’.
36. Use BETWEEN to get employees with salary between 50k and 80k.
37. Use LIKE to find names containing ‘an’.
38. Sort by multiple columns.
39. Fetch NULL records from a column.
40. Replace NULL values using `IFNULL` in a query.

---

## **JOINS**

41. Get all employees and their department names using INNER JOIN.
42. Fetch employees even if they don't have a department using LEFT JOIN.
43. List departments with no employees (RIGHT JOIN or LEFT JOIN).
44. Join three tables: employees, departments, locations.
45. Use a self-join to find employees with the same manager.

---

## **SUBQUERIES**

46. Get employees who earn more than the average salary.
47. Select users who placed more orders than the average number of orders.
48. Find the employee with the highest salary using a subquery.
49. Delete users who placed zero orders using subquery.
50. Select all products whose price is higher than all their category average prices.
51. Use correlated subquery to fetch each employee with their department’s avg salary.

---

## **TCL (Transaction Control)**

52. Write a transaction block using START TRANSACTION, COMMIT, and ROLLBACK.
53. Update multiple rows in a transaction and intentionally roll back.
54. Demonstrate SAVEPOINT and ROLLBACK TO SAVEPOINT.
55. Simulate money transfer between accounts with transaction consistency.

---

## **ADVANCED / MISC**

56. Use window functions to rank employees by salary.
57. Use LEAD/LAG to compare current row salary with previous row salary.
58. Create a stored procedure to return employee details.
59. Create a trigger to update `updated_at` on every row update.
60. Use JSON_EXTRACT to select fields from a JSON column.
61. Write a query to pivot rows into columns using conditional aggregation.
62. Use CTE (WITH clause) to list top 3 salaries from each department.
63. Create an event (scheduler) that cleans old logs daily.
64. Explain and write a query using `EXPLAIN ANALYZE`.
65. Write a recursive CTE to generate numbers 1 to 10.
66. Query to detect duplicate rows based on email.
67. Delete all duplicates while keeping only the latest entry.
68. Write a query to find gaps in an ID sequence.
69. Implement soft delete using `is_deleted` flag.
70. Select most frequently purchased product.

---

This should keep your SQL neurons nicely caffeinated. Dive into a few queries at a time, and the patterns start appearing like constellations in a well-behaved galaxy.
