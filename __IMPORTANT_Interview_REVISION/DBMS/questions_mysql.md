Here comes a buffet of 50+ MySQL practice questions — pure questions only, neatly grouped by **DDL**, **DML**, **DQL**, **TCL**, **Joins**, **Subqueries**, and **Misc**. Perfect for drilling your SQL muscles.

---

# **MySQL Practice Questions (Copy-Friendly Markdown)**

## **DDL (Data Definition Language)**

1. Create a table `employees` with id, name, salary, and department.

```sql
CREATE TABLE employees (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    salary DECIMAL(10, 2) NOT NULL CHECK (salary > 0),
    department VARCHAR(50)
);
```

2. Alter a table to add a new column `created_at` with default current timestamp.
```sql
ALTER TABLE employees ADD COLUMN created_at DATETIME DEFAULT CURRENT_TIMESTAMP;
```

3. Alter a column datatype from INT to BIGINT.
```sql
ALTER TABLE employees MODIFY COLUMN id BIGINT;
```
4. Drop a column from a table.
```sql
ALTER TABLE employees DROP COLUMN department;
```

> or

```sql
ALTER TABLE employees DROP department;
```

5. Rename a table from `orders` to `customer_orders`.
```sql
CREATE TABLE orders(
    name VARCHAR(100)
);
RENAME TABLE orders to customer_orders;
```
6. Create a table with a foreign key referencing another table.
```sql
CREATE TABLE department (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE employees (
    id INT PRIMARY KEY AUTO_INCREMENT,
    dept_id INT NOT NULL,
    FOREIGN KEY (dept_id) REFERENCES department(id)
);

CREATE TABLE tasks (
    id INT PRIMARY KEY AUTO_INCREMENT,
    task_name VARCHAR(255) NOT NULL,
    task_description VARCHAR(500) NOT NULL,
    starts_at DATETIME,
    ends_at DATETIME
);

CREATE TABLE user_task (
    u_id INT NOT NULL,
    t_id INT NOT NULL,
    PRIMARY KEY (u_id, t_id),
    FOREIGN KEY (u_id) REFERENCES employees(id),
    FOREIGN KEY (t_id) REFERENCES tasks(id)
);

```

7. Create a composite primary key on two columns.
```sql
CREATE TABLE students (
    id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE courses (
    id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE registrations (
    s_id INT NOT NULL,
    c_id INT NOT NULL,
    PRIMARY KEY (s_id, c_id),
    FOREIGN KEY (s_id) REFERENCES students(id),
    FOREIGN KEY (c_id) REFERENCES courses(id)
);

```

8. Add a UNIQUE constraint to the `email` column.
```sql
CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE
);
```

9. Remove a primary key from a table.
```sql
ALTER TABLE planets
DROP PRIMARY KEY;

```
- After this, the AUTO_INCREMENT on id is silently stripped away because it only works on a primary key or on a unique key. The column becomes an ordinary integer flapping in the solar wind.

10. Change a column name in a table.
```sql
ALTER TABLE department RENAME COLUMN full_name TO name;
```

- old syntax 5

```sql
ALTER TABLE department CHANGE COLUMN full_name name VARCHAR(100);
```

11. Create an index on `last_name` column.

```sql
ALTER TABLE employees ADD COLUMN last_name VARCHAR(255) NOT NULL;
CREATE INDEX idx_last_name ON employees(last_name);
```

12. Create a full-text index on a `description` column.
```sql
ALTER TABLE employees ADD COLUMN description TEXT;
CREATE FULLTEXT INDEX f_tx_idx_desc ON employees(description);
```

13. Drop an index from a table.

```sql
DROP INDEX f_tx_idx_desc ON employees;
```

- official syntax

```sql
ALTER TABLE employees DROP INDEX f_tx_idx_desc;
```


14. Create a table using `CHECK` constraint (MySQL 8+).
```sql
CREATE TABLE check_op (
    name VARCHAR(100) NOT NULL,
    age INT CHECK(age > 18 AND age < 110)
);
```
15. Create a view named `active_users` that filters only active users.
```sql
CREATE VIEW adult_users AS SELECT e.last_name, e.age FROM employees e WHERE e.age > 18;
```
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
