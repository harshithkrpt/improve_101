
1. ROW_NUMBER()

- Gives a unique sequential number per row within a window (partition), even if values tie.

```sql
SELECT name, dept, salary, ROW_NUMBER() OVER (PARTITION BY dept ORDER BY salary DESC) as rn FROM employees;
```

2. RANK()

Assigns rank with gaps. Tied values share the same rank.

```sql
SELECT 
    name, dept, salary,
    RANK() OVER (PARTITION BY dept ORDER BY salary DESC) AS rnk
FROM employees;

```

| name    | salary | rnk |
| ------- | ------ | --- |
| Bharath | 70000  | 1   |
| Chaitra | 70000  | 1   |
| Asha    | 50000  | 3   |

3. Same as RANK() but no gaps in ranking.

```sql
SELECT 
    name, dept, salary,
    DENSE_RANK() OVER (PARTITION BY dept ORDER BY salary DESC) AS rnk
FROM employees;
```

| name    | salary | drnk |
| ------- | ------ | ---- |
| Bharath | 70000  | 1    |
| Chaitra | 70000  | 1    |
| Asha    | 50000  | 2    |


4. LAG()

- Reaches back to the previous row (based on ordering) without self-joins.

```sql
SELECT
    name, dept, salary,
    LAG(salary) OVER (PARTITION BY dept ORDER BY salary) AS prev_salary
FROM employees;

```

| name    | salary | prev_salary |
| ------- | ------ | ----------- |
| Asha    | 50000  | NULL        |
| Bharath | 70000  | 50000       |
| Chaitra | 70000  | 70000       |


5. LEAD()

- Like LAG, but peeks forward into the next row.

```sql
SELECT
    name, dept, salary,
    LEAD(salary) OVER (PARTITION BY dept ORDER BY salary) AS next_salary
FROM employees;
```

| name    | salary | next_salary |
| ------- | ------ | ----------- |
| Asha    | 50000  | 70000       |
| Bharath | 70000  | 70000       |
| Chaitra | 70000  | NULL        |
