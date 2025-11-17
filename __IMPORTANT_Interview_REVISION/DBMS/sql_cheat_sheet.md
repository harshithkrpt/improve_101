
## Creating Tables - Data Defination Language


- direct primary key tables

```sql
CREATE TABLE users(
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE teams (
    team_id INT PRIMARY KEY AUTO_INCREMENT,
    team_name VARCHAR(100) NOT NULL UNIQUE
);
```

- Simple Foreign Key

```sql
CREATE TABLE members (
    member_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);
```


- foreign key with cascade on delete / on update

```sql
CREATE TABLE user_profiles (
    profile_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    bio TEXT,
    FOREIGN KEY (user_id) REFERENCES users(user_id) 
        ON DELETE CASCADE
        ON UPDATE CASCADE
);
```

- foreign key inline 

```sql
CREATE TABLE tasks (
    task_id INT PRIMARY KEY AUTO_INCREMENT,
    assigned_to INT NOT NULL REFERENCES users(user_id),
    description VARCHAR(255)
);

```

- composite primary key + foreign key

```sql
CREATE TABLE team_membership (
    user_id INT NOT NULL,
    team_id INT NOT NULL,
    PRIMARY KEY (user_id, team_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (team_id) REFERENCES teams(team_id) ON DELETE CASCADE
);
```


- junction table or many to many relation ships

```sql
CREATE TABLE projects (
    project_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(100)
);

CREATE TABLE user_projects (
    user_id INT,
    project_id INT,
    PRIMARY KEY (user_id, project_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (project_id) REFERENCES projects(project_id)
);
```

- Self Referencing Foreign Key

```sql
CREATE TABLE employees (
    emp_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    manager_id INT,
    FOREIGN KEY (manager_id) REFERENCES employees(emp_id) ON DELETE SET NULL
);
```

- Foreign Key with RESTRICT

> RESTRICT means "don’t even think about deleting."

```sql
CREATE TABLE invoices (
    invoice_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    amount DECIMAL(10, 2),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
        ON DELETE RESTRICT
        ON UPDATE RESTRICT
);
```

- Multiple Foreign keys to Multiple Tables
> Tables juggling relationships like a circus.

```sql
CREATE TABLE comments (
    comment_id INT PRIMARY KEY,
    comment TEXT,
    user_id INT NOT NULL,
    project_id INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (project_id) REFERENCES projects(project_id)
);
```


- Table with Check Constriants

```sql
CREATE TABLE orders (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    amount DECIMAL(10,2),
    status ENUM('PENDING', 'PAID', 'CANCELLED'),
    CHECK (amount >= 0)
);
```



### Window Functions

- Table Creation

```sql
CREATE TABLE baby_names (
    gender ENUM('Girl', 'Boy') NOT NULL,
    name VARCHAR(255) NOT NULL,
    total INT NOT NULL
);
```

- Row Number based on popularity 

```sql
SELECT
	Gender ,
	Name,
	Total ,
	ROW_NUMBER() OVER(ORDER BY Total DESC) As Popularity
FROM
	baby_names;
```

- Different Functions

```sql
SELECT 
    Gender, 
    Age,
    Total,
    ROW_NUMBER() OVER(ORDER BY Total DESC) AS Popularity,
    RANK() OVER(ORDER BY Total DESC) AS Popularity_R,
    DENSE_RANK() OVER (ORDER BY Total DESC) AS Popularity_Dr
FROM baby_names;
```

- Partition By simillar to group by but for window

```sql
SELECT gender, name , total
        ROW_NUMBER() OVER(PARTITION BY gender ORDER BY total DESC) AS popularity
FROM baby_names;
```

- retual all the genders top 3 most used names

```sql
SELECT * FROM (SELECT
	gender,
	name ,
	total,
        ROW_NUMBER() OVER(PARTITION BY gender ORDER BY total DESC) AS popularity
FROM
	baby_names) AS P WHERE P.popularity <= 3;
```



### Locks - In Mysql

A database is like a busy food court. Many hungry clients want to read and write data at the same time. Locks keep things consistent so one person’s burger order doesn’t overwrite another’s dosa.


#### 🔹 1. Table Locks (the giant “Everyone wait!” lock)

Table locks are the blunt instrument of MySQL.

When MySQL takes a table-level lock, it locks the entire table.

Two flavours:

1. READ LOCK
Multiple clients can read the table, nobody can write.

2. WRITE LOCK
Only one client can write. All readers must wait.

MyISAM relies on table locks heavily. InnoDB uses them occasionally but prefers row-level locks.

#### 🔹 2. Row Locks (precision surgery, InnoDB style)

- InnoDB uses row-level locks for most operations. They let MySQL lock only the specific rows needed.

Two primary types:

1. Shared Lock (S Lock)

- shared lock lets you read the row but not modify it
- multiple shared locks can co exist

```sql
SELECT * FROM users WHERE id = 10 FOR SHARE;
```

2. Exclusive Lock (X Lock)

- I am updating it no body can read or write to it

```sql
SELECT * FROM users WHERE id = 10 FOR UPDATE;
```

#### 🔹 3. Gap Locks (“Don’t insert anything between these values”)

- Gap locks lock a range of value between them not the rows themselves

```sql
SELECT * FROM users WHERE age BETWEEN 20 AND 30 FOR UPDATE;
```

- InnoDB lock:
    - Existing rows.
    - The gaps between them to prevent phantom inserts.

- Gap locks exist mainly in REPEATABLE READ isolation level.

### 🔹 4. Next-Key Locks (row + gap combo meal)

A next-key lock = row lock + gap lock around it.

So for row with id=10, the lock covers:

- the row itself.
- the gap before it.

This is MySQL’s default strategy in REPEATABLE READ to avoid phantom reads.
Next-key locks are why some innocent-looking queries suddenly block inserts.

### 🔹 5. Intention Locks (meta-locks)

- These are not actual locks on data… they are signals.
InnoDB uses them to announce its intentions.

Intention Shared (IS): “I’m going to put shared locks on some rows.”
Intention Exclusive (IX): “I’m going to lock some rows exclusively.”

### 🔹 6. Auto-Increment Locks

- When inserting new rows into an auto-increment column, MySQL may create a special lock to avoid duplicate values.
- “Auto-inc lock per insert” → only holds the lock during the insertion, not during the whole transaction.

### 🔹 7. Metadata Locks (MDL)

- These lock the definition of a table—not its data.

🔬 Isolation levels and how they change locking

MySQL defaults to REPEATABLE READ.

Impact:

REPEATABLE READ uses next-key locks → prevents phantom reads.

READ COMMITTED reduces gap locks → higher concurrency, less safety.

Interview tip:
If they ask “What is the default isolation level?” the safe answer is:
REPEATABLE READ for InnoDB.


#### Questions and answers on locks

1. What MySQL actually locks ?

MySQL doesn’t just lock “data.” It locks:

- Tables
- Rows
- Ranges
- Even Metadata
- Auto Increment Counter

Each lock type solves a different kind of chaos.


2. Storage Engine decides lock ?

InnoDB is the star here.
MyISAM uses table locks only.
InnoDB is row-locking, transactional, and uses multiple fancy lock types.


- Topic Wise Most Asked Questions -> Theory Query Level

---

### Basics

> Databases, tables, rows, columns, data types, constraints, NULL rules

- **Databases are containers**
    - A database is a logical bucket holding tables, indexes, views—almost like a file system built for structured thinking.

- **Tables are grids**
    - Each table is a structured sheet with rows (records) and columns (fields). Think of it as the strict version of an Excel sheet that won’t tolerate chaos.

- **Rows are instances**
    - Each row represents an entity: one user, one transaction, one chocolate bar with questionable calories.

- **Columns are attributes**
    - Columns define what fields each row must speak. Each has a name and a data type.

- **Data types are shape restrictions**
    - Examples: INT, BIGINT, VARCHAR, DATE, DECIMAL, JSON, TEXT.
    - They determine the binary footprint and valid operations.

- **Constraints are rules**
    - They enforce order: PRIMARY KEY, UNIQUE, NOT NULL, CHECK, FOREIGN KEY, DEFAULT.
    - They’re the bouncers who decide what enters the table.

- **NULL means “unknown / not applicable,” not “empty” and definitely not “zero.”**
    - The philosophical prankster of SQL—it complicates comparisons and needs special handling (IS NULL instead of =).


### Questions on Basics : 

- What is the difference between a database and a table ?
    - A database stores multiple tables and related objects; a table stores structured records in rows and columns.

- What is a primary key? Why is it important?
    - A column or set of columns that uniquely identifies each row. No duplicates, no NULLs. Essential for indexing and relationships.

- Difference between PRIMARY KEY and UNIQUE?
    -  Both enforce uniqueness. Primary key cannot be NULL and only one is allowed per table. UNIQUE allows NULLs and you can have multiple.

- What is a foreign key?
    - A reference from one table to a primary (or unique) key of another table, enforcing referential integrity.

- What is the difference between CHAR and VARCHAR?
    - CHAR is fixed-length (padded), fast for uniform strings. VARCHAR is variable-length, more space-efficient for unpredictable lengths.

- What is a constraint? Name types of constraints.
    - A rule that controls data integrity. Common: PRIMARY KEY, UNIQUE, NOT NULL, FOREIGN KEY, CHECK, DEFAULT.

- What is a NULL value? Is NULL = NULL?
    - NULL means “unknown.” NULL = NULL is false.
    - You must use IS NULL to check.

- What are indexes? Why are they used?
    - Indexes are data structures (B+Trees by default) used to speed up lookups but at the cost of extra space and slower writes.


---