

---

# ✅ **Most Asked / Most Important MySQL Keywords (Interview-Focused)**

These are grouped the way interviewers think, not the way textbooks do.

---

## **🔹 1. Table & Schema Definition (DDL)**

```md
CREATE
ALTER
DROP
TRUNCATE
RENAME
PRIMARY KEY
FOREIGN KEY
UNIQUE
CHECK
DEFAULT
NOT NULL
AUTO_INCREMENT
INDEX
CONSTRAINT
```

---

## **1) CREATE**

```sql
CREATE TABLE employees (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    salary DECIMAL(10,2) DEFAULT 0,
    department_id INT
);
```

---

## **2) ALTER**

Add column:

```sql
ALTER TABLE employees ADD email VARCHAR(100);
```

Modify column:

```sql
ALTER TABLE employees MODIFY salary DECIMAL(12,2);
```

Add constraint:

```sql
ALTER TABLE employees ADD CONSTRAINT chk_salary CHECK (salary >= 0);
```

---

## **3) DROP**

```sql
DROP TABLE employees;
```

Drop a column:

```sql
ALTER TABLE employees DROP COLUMN email;
```

---

## **4) TRUNCATE**

```sql
TRUNCATE TABLE employees;
```

---

## **5) RENAME**

Rename table:

```sql
RENAME TABLE employees TO staff;
```

Rename column:

```sql
ALTER TABLE staff RENAME COLUMN salary TO base_salary;
```

---

## **6) PRIMARY KEY**

Inline:

```sql
CREATE TABLE teams (
    team_id INT PRIMARY KEY,
    team_name VARCHAR(100)
);
```

Separate:

```sql
CREATE TABLE departments (
    dept_id INT,
    dept_name VARCHAR(100),
    PRIMARY KEY (dept_id)
);
```

---

## **7) FOREIGN KEY**

```sql
CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    dept_id INT,
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
);
```

With constraint name:

```sql
ALTER TABLE employees
ADD CONSTRAINT fk_emp_dept
FOREIGN KEY (dept_id) REFERENCES departments(dept_id);
```

---

## **8) UNIQUE**

```sql
CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(150) UNIQUE
);
```

Add UNIQUE later:

```sql
ALTER TABLE users ADD CONSTRAINT uniq_email UNIQUE (email);
```

---

## **9) CHECK**

```sql
CREATE TABLE products (
    id INT PRIMARY KEY,
    price DECIMAL(10,2),
    stock INT,
    CHECK (price >= 0 AND stock >= 0)
);
```

---

## **10) DEFAULT**

```sql
CREATE TABLE orders (
    id INT PRIMARY KEY,
    status VARCHAR(20) DEFAULT 'PENDING',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## **11) NOT NULL**

```sql
CREATE TABLE books (
    id INT PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    author VARCHAR(200) NOT NULL
);
```

---

## **12) AUTO_INCREMENT**

```sql
CREATE TABLE logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    message TEXT
);
```

---

## **13) INDEX**

Create index:

```sql
CREATE INDEX idx_emp_name ON employees(name);
```

Composite index:

```sql
CREATE INDEX idx_emp_dept_salary ON employees(dept_id, salary);
```

Drop index:

```sql
DROP INDEX idx_emp_name ON employees;
```

---

## **14) CONSTRAINT**

Named primary key:

```sql
CREATE TABLE accounts (
    acc_id INT,
    acc_number VARCHAR(50),
    CONSTRAINT pk_account PRIMARY KEY (acc_id)
);
```

Named foreign key:

```sql
ALTER TABLE accounts
ADD CONSTRAINT fk_acc_user FOREIGN KEY (acc_id) REFERENCES users(id);
```

Named unique:

```sql
ALTER TABLE accounts ADD CONSTRAINT uniq_acc_number UNIQUE(acc_number);
```

Named check:

```sql
ALTER TABLE accounts ADD CONSTRAINT chk_accnum CHECK (CHAR_LENGTH(acc_number) >= 5);
```

---




---

## **🔹 2. Querying Data (DQL)**

```md
SELECT
FROM
WHERE
GROUP BY
HAVING
ORDER BY
DISTINCT
LIMIT
OFFSET
BETWEEN
LIKE
IN
EXISTS
IS NULL
CASE
```

---

 These are the DQL (Data Query Language) superstars, so let's give each its own clean, runnable MySQL example. No fluff, just crisp queries you can plug into any sample schema.

To keep everything coherent, assume these sample tables exist:

```sql
CREATE TABLE employees (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    salary DECIMAL(10,2),
    department VARCHAR(50),
    age INT
);

CREATE TABLE departments (
    id INT PRIMARY KEY AUTO_INCREMENT,
    dept_name VARCHAR(50)
);
```

Now each keyword with multiple sample queries:

---

## SELECT

```sql
SELECT name, salary FROM employees;
```

With expression:

```sql
SELECT name, salary * 12 AS yearly_salary FROM employees;
```

---

## FROM

```sql
SELECT e.name, d.dept_name
FROM employees e
JOIN departments d ON d.id = e.id;
```

---

## WHERE

```sql
SELECT name, salary 
FROM employees
WHERE salary > 50000;
```

Multiple conditions:

```sql
SELECT name FROM employees WHERE salary > 30000 AND age < 30;
```

---

## GROUP BY

```sql
SELECT department, AVG(salary)
FROM employees
GROUP BY department;
```

---

## HAVING

```sql
SELECT department, AVG(salary) AS avg_sal
FROM employees
GROUP BY department
HAVING AVG(salary) > 60000;
```

---

## ORDER BY

```sql
SELECT name, salary
FROM employees
ORDER BY salary DESC;
```

Multi-column:

```sql
SELECT name, department, salary
FROM employees
ORDER BY department ASC, salary DESC;
```

---

## DISTINCT

```sql
SELECT DISTINCT department FROM employees;
```

Multiple fields:

```sql
SELECT DISTINCT department, age FROM employees;
```

---

## LIMIT

```sql
SELECT name, salary FROM employees LIMIT 5;
```

---

## OFFSET

```sql
SELECT name FROM employees LIMIT 5 OFFSET 10;
```

---

## BETWEEN

```sql
SELECT name, salary
FROM employees
WHERE salary BETWEEN 40000 AND 70000;
```

With dates example:

```sql
SELECT *
FROM attendance
WHERE date BETWEEN '2024-01-01' AND '2024-01-31';
```

---

## LIKE

```sql
SELECT name FROM employees WHERE name LIKE 'A%';
```

Contains:

```sql
SELECT name FROM employees WHERE name LIKE '%son%';
```

---

## IN

```sql
SELECT name 
FROM employees 
WHERE department IN ('HR', 'Finance');
```

---

## EXISTS

```sql
SELECT *
FROM employees e
WHERE EXISTS (
    SELECT 1 
    FROM departments d 
    WHERE d.id = e.id
);
```

---

## IS NULL

```sql
SELECT name FROM employees WHERE department IS NULL;
```

Negation:

```sql
SELECT name FROM employees WHERE department IS NOT NULL;
```

---

## CASE

```sql
SELECT 
    name,
    salary,
    CASE 
        WHEN salary > 80000 THEN 'High'
        WHEN salary BETWEEN 50000 AND 80000 THEN 'Medium'
        ELSE 'Low'
    END AS salary_band
FROM employees;
```

Nested example:

```sql
SELECT 
    name,
    CASE 
        WHEN age < 25 THEN 'Junior'
        WHEN age BETWEEN 25 AND 40 THEN 'Mid-Level'
        ELSE 'Senior'
    END AS experience_level
FROM employees;
```

---




## **🔹 3. Joins (Core Interview Section)**

```md
INNER JOIN
LEFT JOIN
RIGHT JOIN
FULL OUTER JOIN (simulated in MySQL)
CROSS JOIN
SELF JOIN
ON
USING
```

 Below I give realistic schemas, several common/harder interview-style questions for each JOIN keyword, and ready-to-run query examples (MySQL-flavored). Short explanation after each query so you can quickly tell the interviewer why it’s correct.

---

# Schemas used in examples

```sql
CREATE TABLE employees (
  emp_id INT PRIMARY KEY,
  name VARCHAR(100),
  dept_id INT,
  manager_id INT,     -- references employees.emp_id
  hire_date DATE
);

CREATE TABLE departments (
  dept_id INT PRIMARY KEY,
  dept_name VARCHAR(100),
  location VARCHAR(100)
);

CREATE TABLE salaries (
  emp_id INT,
  salary DECIMAL(10,2),
  from_date DATE,
  to_date DATE
);

CREATE TABLE projects (
  project_id INT PRIMARY KEY,
  project_name VARCHAR(100),
  lead_emp_id INT    -- references employees.emp_id
);

CREATE TABLE tasks (
  task_id INT PRIMARY KEY,
  project_id INT,
  assigned_emp_id INT,
  status VARCHAR(20)
);

CREATE TABLE customers (
  customer_id INT PRIMARY KEY,
  name VARCHAR(100),
  city VARCHAR(100)
);

CREATE TABLE orders (
  order_id INT PRIMARY KEY,
  customer_id INT,
  order_total DECIMAL(10,2),
  order_date DATE
);
```

---

# INNER JOIN

Selects rows that match in both tables.

**Q1 — Basic:** Get employee name + department name.

```sql
SELECT e.emp_id, e.name, d.dept_name
FROM employees e
INNER JOIN departments d
  ON e.dept_id = d.dept_id;
```

*Why:* returns only employees assigned to an existing dept.

**Q2 — Aggregation with join:** Top 5 departments by average salary.

```sql
SELECT d.dept_name, AVG(s.salary) AS avg_salary
FROM departments d
JOIN employees e ON e.dept_id = d.dept_id
JOIN salaries s ON s.emp_id = e.emp_id
WHERE s.to_date IS NULL   -- current salary
GROUP BY d.dept_name
ORDER BY avg_salary DESC
LIMIT 5;
```

*Why:* joins employees to salaries, then groups per department.

**Q3 — Inner join with filters (index-friendly):** Active tasks for employees hired after 2020.

```sql
SELECT e.name, p.project_name, t.status
FROM employees e
JOIN tasks t ON t.assigned_emp_id = e.emp_id
JOIN projects p ON p.project_id = t.project_id
WHERE e.hire_date >= '2021-01-01' AND t.status = 'IN_PROGRESS';
```

---

# LEFT JOIN (LEFT OUTER JOIN)

Return all rows from left table; matching right rows or NULLs.

**Q1 — Find employees without current salary rows (missing data):**

```sql
SELECT e.emp_id, e.name, s.salary
FROM employees e
LEFT JOIN salaries s ON s.emp_id = e.emp_id AND s.to_date IS NULL
WHERE s.emp_id IS NULL;
```

*Why:* identifies employees missing a “current” salary.

**Q2 — Show all departments and their headcount (including zero):**

```sql
SELECT d.dept_name, COUNT(e.emp_id) AS emp_count
FROM departments d
LEFT JOIN employees e ON e.dept_id = d.dept_id
GROUP BY d.dept_name;
```

**Q3 — Orders with optional customer info (defensive reporting):**

```sql
SELECT o.order_id, o.order_total, c.name, c.city
FROM orders o
LEFT JOIN customers c ON o.customer_id = c.customer_id;
```

*Why:* preserves orders even if customer row absent.

---

# RIGHT JOIN (RIGHT OUTER JOIN)

Return all rows from right table; matching left rows or NULLs. (Less common but interviewer may ask.)

**Q1 — Departments that have no employees (alternate to LEFT JOIN):**

```sql
SELECT e.emp_id, e.name, d.dept_name
FROM employees e
RIGHT JOIN departments d ON d.dept_id = e.dept_id
WHERE e.emp_id IS NULL;
```

*Why:* finds departments with zero employees; equivalent to LEFT JOIN reversed.

**Q2 — Ensure all salaries are shown and employee info if exists:**

```sql
SELECT s.emp_id, e.name, s.salary
FROM salaries s
RIGHT JOIN employees e ON e.emp_id = s.emp_id
WHERE s.to_date IS NULL;
```

*Note:* RIGHT JOIN is identical to flipping LEFT JOIN; most teams prefer LEFT JOIN for readability.

---

# FULL OUTER JOIN (simulated in MySQL)

MySQL lacks FULL OUTER; simulate with UNION of LEFT and RIGHT excluding double-count.

**Q1 — Show all employees and salary records whether matched or not:**

```sql
-- Simulate FULL OUTER JOIN employees <-> salaries (current records)
SELECT e.emp_id, e.name, s.salary
FROM employees e
LEFT JOIN salaries s ON s.emp_id = e.emp_id AND s.to_date IS NULL

UNION

SELECT e.emp_id, e.name, s.salary
FROM employees e
RIGHT JOIN salaries s ON s.emp_id = e.emp_id AND s.to_date IS NULL
WHERE e.emp_id IS NULL;
```

*Why:* LEFT covers employees; RIGHT adds salary-only rows; WHERE prevents duplicates.

**Q2 — All customers and orders (even orphan orders or orphan customers):**

```sql
SELECT c.customer_id, c.name, o.order_id, o.order_total
FROM customers c
LEFT JOIN orders o ON o.customer_id = c.customer_id

UNION

SELECT c.customer_id, c.name, o.order_id, o.order_total
FROM customers c
RIGHT JOIN orders o ON o.customer_id = c.customer_id
WHERE c.customer_id IS NULL;
```

---

# CROSS JOIN

Cartesian product — useful in combinatorics, matrix-building, or when pairing every left with every right.

**Q1 — Generate all possible project-owner and task-status combinations for a report:**

```sql
SELECT p.project_name, t.status
FROM projects p
CROSS JOIN (SELECT DISTINCT status FROM tasks) t;
```

*Why:* pairs every project with each distinct status.

**Q2 — Create date + department grid for scheduling (dates table simulation):**

```sql
-- Assume small in-memory date list
SELECT d.dept_name, dt.the_date
FROM departments d
CROSS JOIN (
  SELECT '2025-12-01' AS the_date UNION ALL
  SELECT '2025-12-02' UNION ALL
  SELECT '2025-12-03'
) dt;
```

*Warning:* CROSS JOINs explode rows; use carefully.

---

# SELF JOIN

Join a table to itself — common for hierarchical data like managers.

**Q1 — Employee and their direct manager name:**

```sql
SELECT e.emp_id, e.name AS employee, m.emp_id AS manager_id, m.name AS manager
FROM employees e
LEFT JOIN employees m ON e.manager_id = m.emp_id;
```

**Q2 — Peer lookup: find pairs of employees in same dept (avoid duplicates):**

```sql
SELECT a.emp_id, a.name AS emp_a, b.emp_id, b.name AS emp_b
FROM employees a
JOIN employees b ON a.dept_id = b.dept_id AND a.emp_id < b.emp_id;
```

*Why:* `a.emp_id < b.emp_id` prevents mirrored duplicates and self-pairing.

**Q3 — Find manager chain two levels up (if exists):**

```sql
SELECT e.name AS employee, mgr.name AS manager, mgr2.name AS grand_manager
FROM employees e
LEFT JOIN employees mgr ON e.manager_id = mgr.emp_id
LEFT JOIN employees mgr2 ON mgr.manager_id = mgr2.emp_id;
```

---

# ON vs USING (join condition styles)

**Using `ON` for complex conditions (recommended when columns differ or complex logic):**

```sql
SELECT e.emp_id, e.name, d.dept_name
FROM employees e
JOIN departments d ON e.dept_id = d.dept_id AND d.location = 'Bangalore';
```

*Why:* `ON` allows multiple expressions and non-equi joins.

**Using `USING` when column name(s) identical and you want single output column:**

```sql
SELECT e.emp_id, e.name, d.dept_name
FROM employees e
JOIN departments d USING (dept_id);
```

*Behavior:* `USING` collapses `dept_id` to a single column in result (no table qualifier) — tidy but only for same-named columns.

**Interview bait — show difference with ambiguous column names:**

```sql
-- Using ON keeps qualifiers possible
SELECT e.dept_id AS e_dept, d.dept_id AS d_dept, e.name, d.dept_name
FROM employees e
JOIN departments d ON e.dept_id = d.dept_id;

-- Using USING removes duplicate column names from output
SELECT dept_id, name, dept_name
FROM employees e
JOIN departments d USING (dept_id);
```

---

# CROSS-QUESTION TYPES & trickier interview prompts (with queries)

**Q — “Find employees who have worked on every project.”** (Relational division)

```sql
SELECT e.emp_id, e.name
FROM employees e
WHERE NOT EXISTS (
  SELECT 1 FROM projects p
  WHERE NOT EXISTS (
    SELECT 1 FROM tasks t
    WHERE t.project_id = p.project_id AND t.assigned_emp_id = e.emp_id
  )
);
```

*Why:* classic double-NOT-EXISTS.

**Q — “Find departments where average salary > company average.”**

```sql
SELECT d.dept_name, AVG(s.salary) AS dept_avg
FROM departments d
JOIN employees e ON e.dept_id = d.dept_id
JOIN salaries s ON s.emp_id = e.emp_id
WHERE s.to_date IS NULL
GROUP BY d.dept_name
HAVING AVG(s.salary) > (
  SELECT AVG(salary) FROM salaries WHERE to_date IS NULL
);
```

**Q — “Detect duplicate orders that reference same customer + amount on same day (self-join).”**

```sql
SELECT o1.order_id, o2.order_id, o1.customer_id, o1.order_total, o1.order_date
FROM orders o1
JOIN orders o2
  ON o1.customer_id = o2.customer_id
  AND o1.order_total = o2.order_total
  AND o1.order_date = o2.order_date
  AND o1.order_id < o2.order_id;
```

**Q — “Union vs JOIN: get all unique employees who are either project leads OR have active tasks.”**

```sql
SELECT DISTINCT emp_id, name FROM (
  SELECT p.lead_emp_id AS emp_id, e.name
  FROM projects p JOIN employees e ON p.lead_emp_id = e.emp_id
  UNION
  SELECT t.assigned_emp_id AS emp_id, e2.name
  FROM tasks t JOIN employees e2 ON t.assigned_emp_id = e2.emp_id
) x;
```

---

# Performance / interview talking points to rehearse

* `JOIN` order matters conceptually; the optimizer rewrites, but proper indexes (foreign keys, join columns) are essential.
* Prefer `EXISTS` for anti/semijoin patterns when correlated subquery short-circuits matter.
* Avoid `SELECT *` in joins for big result sets (network and memory).
* Watch out for `CROSS JOIN` or missing `ON` producing accidental cartesian products.
* When simulating `FULL OUTER JOIN` consider `UNION ALL` + `WHERE` to control duplicates and preserve performance.


---

## **🔹 4. Data Modification (DML)**

```md
INSERT
INSERT ... SELECT
UPDATE
DELETE
REPLACE
ON DUPLICATE KEY UPDATE
```

**interview-focused SQL DML statements**, each keyword covered with multiple patterns, variations, and trick scenarios.
Keeping it clean, practical, and realistic… the sort of stuff you’d be grilled on when someone wants to test whether you *really* understand DML.

---

## **🔹 INSERT**

### **1. Basic Insert**

```sql
INSERT INTO employees (name, age, salary)
VALUES ('Amit', 28, 65000);
```

### **2. Insert multiple rows**

```sql
INSERT INTO employees (name, age, salary)
VALUES ('Amit', 28, 65000),
       ('Sara', 32, 72000),
       ('John', 29, 55000);
```

### **3. Insert default values**

```sql
INSERT INTO logs DEFAULT VALUES;
```

### **4. Insert NULL explicitly**

```sql
INSERT INTO employees (name, age, salary)
VALUES ('Unknown', NULL, NULL);
```

---

## **🔹 INSERT … SELECT**

### **5. Copy rows from another table**

```sql
INSERT INTO archived_orders (order_id, user_id, price, created_at)
SELECT id, user_id, price, created_at
FROM orders
WHERE created_at < '2024-01-01';
```

### **6. Insert transformed data**

```sql
INSERT INTO users_audit (user_id, old_age, new_age)
SELECT id, age, age + 1
FROM users
WHERE age > 30;
```

### **7. Insert with JOIN**

```sql
INSERT INTO top_customers (user_id, total_spent)
SELECT u.id, SUM(o.price)
FROM users u
JOIN orders o ON o.user_id = u.id
GROUP BY u.id
HAVING SUM(o.price) > 10000;
```

---

## **🔹 UPDATE**

### **8. Basic update**

```sql
UPDATE employees
SET salary = salary + 5000
WHERE age > 35;
```

### **9. Update multiple columns**

```sql
UPDATE products
SET price = price * 1.10,
    updated_at = NOW()
WHERE category = 'Electronics';
```

### **10. Update using a JOIN**

```sql
UPDATE orders o
JOIN payments p ON p.order_id = o.id
SET o.status = 'PAID'
WHERE p.amount >= o.price;
```

### **11. Update using a subquery**

```sql
UPDATE users
SET vip_status = 'YES'
WHERE id IN (
    SELECT user_id FROM orders GROUP BY user_id HAVING SUM(price) > 20000
);
```

### **12. Update using a CASE expression**

```sql
UPDATE employees
SET grade = CASE
    WHEN salary >= 100000 THEN 'A'
    WHEN salary >= 50000 THEN 'B'
    ELSE 'C'
END;
```

---

## **🔹 DELETE**

### **13. Basic delete**

```sql
DELETE FROM employees
WHERE age < 18;
```

### **14. Delete all rows**

```sql
DELETE FROM logs;
```

*(Unlike TRUNCATE, DELETE is row-by-row)*

### **15. Delete using JOIN**

```sql
DELETE o
FROM orders o
LEFT JOIN payments p ON p.order_id = o.id
WHERE p.id IS NULL;
```

### **16. Delete using subquery**

```sql
DELETE FROM users
WHERE id IN (
    SELECT user_id FROM orders GROUP BY user_id HAVING COUNT(*) = 0
);
```

### **17. Delete with LIMIT**

```sql
DELETE FROM login_logs
ORDER BY created_at ASC
LIMIT 1000;
```

---

## **🔹 REPLACE**

**REPLACE** = DELETE row if key exists + INSERT new row.
Used mostly for upserts in MySQL.

### **18. Replace full row**

```sql
REPLACE INTO users (id, name, city)
VALUES (5, 'Rahul', 'Delhi');
```

If `id = 5` exists → deletes old row → inserts this one.

### **19. Replace using unique key**

```sql
REPLACE INTO user_settings (user_id, theme)
VALUES (10, 'dark');
```

If `user_id` is UNIQUE, it acts like an UPSERT (but destructive).

---

## **🔹 ON DUPLICATE KEY UPDATE**

This is the non-destructive UPSERT.

### **20. Insert or update on unique key conflict**

```sql
INSERT INTO products (id, name, price)
VALUES (100, 'Mouse', 500)
ON DUPLICATE KEY UPDATE price = VALUES(price);
```

### **21. Increment value if duplicate**

```sql
INSERT INTO page_views (page_id, views)
VALUES (1, 1)
ON DUPLICATE KEY UPDATE views = views + 1;
```

### **22. Update multiple fields**

```sql
INSERT INTO employees (email, name, salary)
VALUES ('ram@example.com', 'Ram', 60000)
ON DUPLICATE KEY UPDATE
    name = VALUES(name),
    salary = VALUES(salary);
```

### **23. Maintain audit fields**

```sql
INSERT INTO inventory (item_id, qty, updated_at)
VALUES (10, 50, NOW())
ON DUPLICATE KEY UPDATE
    qty = qty + VALUES(qty),
    updated_at = NOW();
```

---



---

## **🔹 5. Aggregations (Most common questions)**

```md
COUNT
SUM
AVG
MIN
MAX
```

Time to unravel the “big five” of SQL aggregation. These are deceptively simple words that interviewers use to poke at edge cases, NULL behavior, grouping logic, and query planning.
Let’s run through each one with multiple interview-focused patterns and gritty little examples that reveal what’s actually going on.

---

## **🔹 COUNT**

**Counting isn’t as innocent as it looks. NULLs change everything.**

### **1. Count all rows**

```sql
SELECT COUNT(*) FROM employees;
```

Counts every row, including ones containing NULLs.

### **2. Count a specific column (NULLs excluded)**

```sql
SELECT COUNT(city) FROM users;
```

Counts only non-NULL `city` values.

### **3. Count distinct**

```sql
SELECT COUNT(DISTINCT department) FROM employees;
```

### **4. Count with a filter**

```sql
SELECT COUNT(*) 
FROM orders
WHERE price > 5000;
```

### **5. Count groups**

```sql
SELECT department, COUNT(*) AS emp_count
FROM employees
GROUP BY department;
```

### **6. Count with JOIN**

```sql
SELECT u.id, u.name, COUNT(o.id) AS total_orders
FROM users u
LEFT JOIN orders o ON o.user_id = u.id
GROUP BY u.id, u.name;
```

---

## **🔹 SUM**

**Interviews love NULL behavior: SUM ignores NULLs.**

### **1. Basic sum**

```sql
SELECT SUM(price) FROM orders;
```

### **2. Sum with group by**

```sql
SELECT user_id, SUM(price) AS total_spent
FROM orders
GROUP BY user_id;
```

### **3. Sum with CASE (conditional sum)**

```sql
SELECT 
    SUM(CASE WHEN status = 'PAID' THEN price END) AS paid_total,
    SUM(CASE WHEN status = 'PENDING' THEN price END) AS pending_total
FROM orders;
```

### **4. Sum with join**

```sql
SELECT c.id, c.name, SUM(o.price)
FROM customers c
JOIN orders o ON o.customer_id = c.id
GROUP BY c.id, c.name;
```

### **5. Sum distinct**

```sql
SELECT SUM(DISTINCT amount) FROM transactions;
```

---

## **🔹 AVG**

AVG = SUM / COUNT, but COUNT ignores NULLs, so AVG ignores NULLs too.

### **1. Basic average**

```sql
SELECT AVG(salary) FROM employees;
```

### **2. Average with group by**

```sql
SELECT department, AVG(salary)
FROM employees
GROUP BY department;
```

### **3. Average with CASE**

```sql
SELECT AVG(CASE WHEN gender = 'M' THEN salary END) AS avg_male_salary
FROM employees;
```

### **4. Average of distinct values**

```sql
SELECT AVG(DISTINCT score) FROM tests;
```

### **5. AVG with JOIN**

```sql
SELECT u.id, AVG(o.price)
FROM users u
JOIN orders o ON o.user_id = u.id
GROUP BY u.id;
```

---

## **🔹 MIN**

MIN returns the lowest non-NULL value.

### **1. Basic min**

```sql
SELECT MIN(salary) FROM employees;
```

### **2. Min per group**

```sql
SELECT department, MIN(age)
FROM employees
GROUP BY department;
```

### **3. Min with date fields**

```sql
SELECT MIN(created_at) AS first_order
FROM orders;
```

### **4. Min with CASE**

```sql
SELECT 
    MIN(CASE WHEN status = 'PAID' THEN created_at END) AS first_paid_order
FROM orders;
```

### **5. Min from a related table (JOIN)**

```sql
SELECT u.id, MIN(o.price)
FROM users u
JOIN orders o ON u.id = o.user_id
GROUP BY u.id;
```

---

## **🔹 MAX**

MAX is the mirror twin of MIN, with the same rules.

### **1. Basic max**

```sql
SELECT MAX(salary) FROM employees;
```

### **2. Max with group by**

```sql
SELECT city, MAX(age)
FROM users
GROUP BY city;
```

### **3. Max date (latest record)**

```sql
SELECT MAX(login_time) AS last_login
FROM login_logs;
```

### **4. Max with CASE**

```sql
SELECT 
    MAX(CASE WHEN status = 'FAILED' THEN attempts END) AS worst_attempts
FROM login_attempts;
```

### **5. Max from joined table**

```sql
SELECT u.id, MAX(o.price) AS biggest_purchase
FROM users u
JOIN orders o ON o.user_id = u.id
GROUP BY u.id;
```

---

## If you want, I can next cover:

• GROUP BY interview traps
• HAVING vs WHERE (classic interview trick)
• Window functions (ROW_NUMBER, RANK, SUM OVER)
• 40 aggregation interview questions

This topic opens into some beautifully strange territory—lots to explore.


---

## **🔹 6. Window Functions (Modern interviews love these)**

```md
ROW_NUMBER
RANK
DENSE_RANK
LEAD
LAG
OVER
PARTITION BY
```

Window functions are where SQL starts feeling like a brain-teasing puzzle box. Modern interviews adore them because they reveal whether someone can think in *rows + context*, not just rows alone.
Here’s a full set of patterns for each function—practical, realistic, and frequently used in interviews.

---

## **ROW_NUMBER**

Assigns a unique sequential number *per partition*, no ties allowed.

### Rank employees by salary within each department

```sql
SELECT 
    id, name, department, salary,
    ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary DESC) AS rn
FROM employees;
```

### Get the top-1 per group (“latest order per user” trick)

```sql
SELECT *
FROM (
    SELECT 
        o.*, 
        ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY created_at DESC) AS rn
    FROM orders o
) x
WHERE rn = 1;
```

---

## **RANK**

Same as `ROW_NUMBER` but ties receive the same rank, with gaps.

### Rank students by score (ties allowed)

```sql
SELECT 
    name, score,
    RANK() OVER (ORDER BY score DESC) AS score_rank
FROM students;
```

### Rank purchases inside each category

```sql
SELECT 
    product, category, price,
    RANK() OVER (PARTITION BY category ORDER BY price DESC) AS rank_in_cat
FROM products;
```

---

## **DENSE_RANK**

Like RANK but *no gaps* in ranking.

### Best-selling product rank, dense

```sql
SELECT 
    product, units_sold,
    DENSE_RANK() OVER (ORDER BY units_sold DESC) AS sales_rank
FROM sales;
```

### Dense rank with partition

```sql
SELECT
    user_id, score,
    DENSE_RANK() OVER (PARTITION BY user_id ORDER BY score DESC) AS attempt_rank
FROM test_attempts;
```

---

## **LAG**

Look at *previous row* (historical comparison).

### Compare current day’s sales with yesterday

```sql
SELECT 
    day,
    sales,
    LAG(sales, 1) OVER (ORDER BY day) AS prev_sales
FROM daily_sales;
```

### Detect price change for products

```sql
SELECT 
    product_id,
    price,
    LAG(price) OVER (PARTITION BY product_id ORDER BY updated_at) AS prev_price
FROM product_price_history;
```

---

## **LEAD**

Opposite of LAG — look at *next row*.

### Find next appointment for each user

```sql
SELECT 
    user_id,
    appointment_time,
    LEAD(appointment_time) OVER (PARTITION BY user_id ORDER BY appointment_time) AS next_appointment
FROM appointments;
```

### Compare current stock level vs upcoming stock level

```sql
SELECT 
    item_id, stock,
    LEAD(stock) OVER (PARTITION BY item_id ORDER BY updated_at) AS next_stock
FROM warehouse_levels;
```

---

## **OVER**

Defines the *window* (partition + ordering + framing).

### Average salary within each department

```sql
SELECT 
    name, department, salary,
    AVG(salary) OVER (PARTITION BY department) AS dept_avg_salary
FROM employees;
```

### Running sum (sliding window)

```sql
SELECT
    day,
    revenue,
    SUM(revenue) OVER (ORDER BY day ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS cumulative_revenue
FROM revenue_daily;
```

---

## **PARTITION BY**

Divides rows logically into groups that window functions operate on.

### Partition login attempts per user

```sql
SELECT 
    user_id,
    login_time,
    ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY login_time) AS attempt_number
FROM login_logs;
```

### Get highest transaction per user (using window)

```sql
SELECT *
FROM (
    SELECT
        t.*,
        RANK() OVER (PARTITION BY user_id ORDER BY amount DESC) AS rnk
    FROM transactions t
) x
WHERE rnk = 1;
```

---

## ⭐ Bonus Interview Patterns (Very common)

### **Find top 3 salaries per department**

```sql
SELECT *
FROM (
    SELECT 
        name, department, salary,
        DENSE_RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS dr
    FROM employees
) x
WHERE dr <= 3;
```

### **Find customers whose spending decreased over time**

```sql
SELECT
    user_id,
    month,
    total_spent,
    LAG(total_spent) OVER (PARTITION BY user_id ORDER BY month) AS prev_spent
FROM monthly_user_spending;
```

### **Find gaps between events**

```sql
SELECT
    event_id,
    event_time,
    event_time - LAG(event_time) OVER (ORDER BY event_time) AS gap
FROM system_events;
```

---

Window functions are the closest SQL gets to time travel—they let you peer into the “past” or “future” of rows without needing self-joins. The next great frontier from here is **window framing**, **moving averages**, **percentile ranking**, and **NTILE** if you're curious.


---

## **🔹 7. Transactions (TCL)**

```md
START TRANSACTION
COMMIT
ROLLBACK
SAVEPOINT
```

---

## **🔹 8. Subqueries & Set Operations**

```md
SUBQUERY
EXISTS
IN
ANY
ALL
UNION
UNION ALL
```

Transactions are where SQL stops being just a query language and starts behaving like a cautious, disciplined machine that refuses to mess up your data unless you *explicitly* say “go ahead.”
Interviewers use these commands to test whether you truly grasp **atomicity**, **rollback logic**, and **partial rollbacks**.

Let’s walk through the practical patterns for each TCL command, all interview-focused and realistic.

---

## **START TRANSACTION**

Opens a controlled block where changes are temporary until committed.

### **1. Basic transaction start**

```sql
START TRANSACTION;

UPDATE accounts SET balance = balance - 500 WHERE id = 1;
UPDATE accounts SET balance = balance + 500 WHERE id = 2;

COMMIT;
```

### **2. With consistent read**

```sql
SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED;
START TRANSACTION;

SELECT * FROM orders WHERE status = 'PENDING';

COMMIT;
```

### **3. Transaction with error handling (manual rollback)**

```sql
START TRANSACTION;

UPDATE products SET stock = stock - 1 WHERE id = 10;

-- Suppose stock goes negative or constraint fails
ROLLBACK;
```

---

## **COMMIT**

Finalizes all changes since the last transaction began.

### **1. Commit banking transfer**

```sql
START TRANSACTION;

UPDATE accounts SET balance = balance - 1000 WHERE id = 5;
UPDATE accounts SET balance = balance + 1000 WHERE id = 8;

COMMIT;
```

### **2. Commit batch inserts**

```sql
START TRANSACTION;

INSERT INTO logs(message) VALUES ('Job started');
INSERT INTO logs(message) VALUES ('Job processing');
INSERT INTO logs(message) VALUES ('Job finished');

COMMIT;
```

### **3. Commit only when validation is correct**

```sql
START TRANSACTION;

UPDATE orders SET status = 'PAID' WHERE id = 100;

-- If everything looks good:
COMMIT;
```

---

## **ROLLBACK**

Undo everything since the start of the transaction.

### **1. Complete rollback**

```sql
START TRANSACTION;

DELETE FROM orders WHERE created_at < '2022-01-01';

ROLLBACK;  -- nothing is deleted
```

### **2. Rollback on failure (simulated)**

```sql
START TRANSACTION;

UPDATE inventory SET qty = qty - 5 WHERE item_id = 10;

-- stock becomes negative → fail
ROLLBACK;
```

### **3. Rollback instead of commit when checks fail**

```sql
START TRANSACTION;

UPDATE employees SET salary = salary + 20000 WHERE id = 7;

-- if salary now crosses policy max limit
ROLLBACK;
```

---

## **SAVEPOINT**

Creates checkpoints within a transaction so you can roll back *part* of it.

### **1. Create & rollback to savepoint**

```sql
START TRANSACTION;

UPDATE accounts SET balance = balance - 500 WHERE id = 1;

SAVEPOINT deduct_done;

UPDATE accounts SET balance = balance + 5000 WHERE id = 2;  -- wrong amount

ROLLBACK TO deduct_done;  -- undo second update only

COMMIT;  -- first part still applied
```

### **2. Multiple savepoints**

```sql
START TRANSACTION;

INSERT INTO temp_table VALUES (1);
SAVEPOINT s1;

INSERT INTO temp_table VALUES (2);
SAVEPOINT s2;

INSERT INTO temp_table VALUES (3);

ROLLBACK TO s2;   -- undo the row '3'

COMMIT;           -- rows 1 and 2 remain
```

### **3. Savepoint inside complex logic**

```sql
START TRANSACTION;

INSERT INTO orders(user_id, price) VALUES (10, 5000);
SAVEPOINT after_insert;

UPDATE users SET total_spent = total_spent + 5000 WHERE id = 10;

-- if update fails
ROLLBACK TO after_insert;

COMMIT;
```

---

## ⭐ Bonus Interview Scenarios

### **1. Transfer money using safe transaction**

```sql
START TRANSACTION;

UPDATE accounts SET balance = balance - 3000 WHERE id = 1;
UPDATE accounts SET balance = balance + 3000 WHERE id = 2;

IF (SELECT balance FROM accounts WHERE id = 1) < 0 THEN
    ROLLBACK;
ELSE
    COMMIT;
END IF;
```

### **2. Delete user + related data atomically**

```sql
START TRANSACTION;

DELETE FROM orders WHERE user_id = 50;
DELETE FROM users WHERE id = 50;

COMMIT;
```

### **3. Avoid partial data corruption**

```sql
START TRANSACTION;

UPDATE inventory SET qty = qty - 10 WHERE item_id = 1;
SAVEPOINT safe_point;

UPDATE inventory SET qty = qty - 100 WHERE item_id = 2;  -- overshoots

ROLLBACK TO safe_point;  -- undo only second update

COMMIT;
```

---

Transactions are the safety net that keeps the database from turning into a haunted mansion of half-updated ghosts.
If you're up for it, I can continue with **isolation levels**, **locking (row locks, table locks)**, or **ACID deep-dive interview traps**—this is where things get properly interesting.


---

## **🔹 9. Performance & Indexing**

```md
EXPLAIN
INDEX
USE INDEX
FORCE INDEX
```

---

## **🔹 10. Views, Procedures, Triggers**

```md
CREATE VIEW
CREATE PROCEDURE
CREATE FUNCTION
CREATE TRIGGER
```

---

## **🔹 11. JSON (Increasingly asked)**

```md
JSON_EXTRACT
JSON_SET
JSON_ARRAY
JSON_OBJECT
```

---

# ⭐ The short list (if you want absolute minimum survival pack)

Interviewers expect you to instantly know these:

```md
SELECT, WHERE, GROUP BY, HAVING, ORDER BY, LIMIT  
INNER JOIN, LEFT JOIN  
COUNT, SUM, AVG  
ROW_NUMBER, RANK, PARTITION BY  
INSERT, UPDATE, DELETE  
PRIMARY KEY, FOREIGN KEY, UNIQUE  
EXISTS, IN, BETWEEN, LIKE  
EXPLAIN, INDEX  
COMMIT, ROLLBACK  
```

---

If you want, I can also give you a **"cheat sheet PDF-style" version**, or the **top 50 trick questions** based on these keywords.


