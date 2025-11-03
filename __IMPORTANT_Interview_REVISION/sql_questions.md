## SQL Questions

### What is a relational database?

- stores data in tables & has relation between the tables as keys
- tables has rows -> records & columns (fields)

### What is SQL and how does it differ from NoSQL?

| Feature        | SQL                 | NoSQL                                  |
| -------------- | ------------------- | -------------------------------------- |
| Data Model     | Relational (tables) | Non-relational (JSON, key-value, etc.) |
| Schema         | Predefined          | Dynamic                                |
| Query Language | SQL                 | Custom or API-based                    |
| Scalability    | Vertical            | Horizontal                             |
| Transactions   | Strong (ACID)       | Flexible (BASE)                        |
| Best For       | Structured data     | Unstructured / rapidly changing data   |

### Explain the difference between DELETE, TRUNCATE and DROP.

- delete
    -> use where clause
    -> can be rolled back
    -> logs each deleted record
    
```sql
delete from employees where department = 'sales';
```

- trucate
    -> delet all rows (no where) 
    -> much faster
    -> resets auto increment counters
    -> cannot be rolled back in most (ddl command)

```sql
DROP TABLE employee;
```

- drop
    -> remove the entire table, including its structure , indexes, data & constraints
    -> Completely deletes the table definition.
    -> Cannot be rolled back once executed.
    -> You’ll need to recreate the table to use it again.

```sql
DROP TABLE employees;
```

### What are primary keys and foreign keys? Why use them?

- primary key is the unique identifier for each record in a table
- it cannot be null & no two rows can have same keys
- can be single or composite

```sql
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100)
);
```

- foreign key is a field or set of fields that links to the primary key of another table
- it enforces referential integrity

```sql
CREATE TABLE orders(
    order_id INT PRIMARY KEY,
    order_date DATE,
    customer_id INT,
    FOREIGN KEY customer_id REFERENCES customers(customer_id)
);
```

```sql
FOREIGN KEY (ID) 
REFERENCES TABLE_NAME(FK_ID)
ON DELETE <OPTION>
ON UPDATE <OPTION>
```

- OPTION 
    - CASCADE 
    - NULL 
    - RESTRICT (DEFAULT)

### What is normalization? Describe 1NF, 2NF, 3NF and BCNF.

- normalization -> reduce data redundancy
- ensure data integrity
- divide large tables into smaller & related ones

- 1st normal form -> "every column must contain atomic values -> values which cannot be divided further"
                  -> "have primary key"

FROM  :

| student_id | name  | subjects         |
| ---------- | ----- | ---------------- |
| 1          | Alice | Math, Science    |
| 2          | Bob   | English, History |


TO : 

| student_id | name  | subject |
| ---------- | ----- | ------- |
| 1          | Alice | Math    |
| 1          | Alice | Science |
| 2          | Bob   | English |
| 2          | Bob   | History |


- 2nd normal form 
    -> follow 1st normal form
    -> all non key attributes mush depend on primary key (whole key not part of the key)

FROM :

| student_id | course_id | student_name | course_name |
| ---------- | --------- | ------------ | ----------- |
| 1          | C1        | Alice        | Math        |
| 1          | C2        | Alice        | Science     |

TO:

| student_id | student_name |
| ---------- | ------------ |
| 1          | Alice        |

| course_id | course_name |
| --------- | ----------- |
| C1        | Math        |
| C2        | Science     |

| student_id | course_id |
| ---------- | --------- |
| 1          | C1        |
| 1          | C2        |


- 3RD normal form
    -> follow 2nf
    -> no transitive dependancy -> non key attributes must depent on primary key not trasitively 

FROM :

| employee_id | employee_name | department_id | department_name |
| ----------- | ------------- | ------------- | --------------- |
| 1           | John          | D1            | HR              |
| 2           | Mary          | D2            | Finance         |


TO:

| employee_id | employee_name | department_id |
| ----------- | ------------- | ------------- |
| 1           | John          | D1            |
| 2           | Mary          | D2            |

| department_id | department_name |
| ------------- | --------------- |
| D1            | HR              |
| D2            | Finance         |


- strictier version of 3rd normal for is bcnf
- removes anomolies 


### What is denormalization and when is it useful?

- reintroducing reduncancy
- combining tables
- undoing some normalisations to improve performance

- useful for read heavy tasks


### Explain ACID properties.

1. Atomicity - A transaction must be all or nothing — either every operation in it succeeds, or the entire transaction is rolled back.
2. Consistency - A transaction must move the database from one valid state to another — maintaining all constraints, triggers, and rules.
3. Isolation - Multiple transactions can occur simultaneously without affecting each other’s outcome.
4. Durability - Once a transaction is committed, it’s permanently saved, even if the system crashes immediately after.

- used in database transactions


### What is a transaction? How do COMMIT and ROLLBACK work?

A transaction in SQL is a sequence of one or more SQL statements that are executed as a single logical unit of work.

```sql
START TRANSACTION;
-- your SQL operations
COMMIT;    -- or ROLLBACK;

```

```sql
START TRANSACTION;

UPDATE accounts
SET balance = balance - 500
WHERE account_id = 1;

UPDATE accounts
SET balance = balance + 500
WHERE account_id = 2;

COMMIT;

```


### What are isolation levels? Explain READ UNCOMMITTED, READ COMMITTED, REPEATABLE READ, and SERIALIZABLE.

