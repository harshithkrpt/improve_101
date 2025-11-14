
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