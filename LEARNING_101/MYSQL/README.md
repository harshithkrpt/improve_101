# Create the markdown content for the e-commerce table structure

ecommerce_schema_md = """
# 🛒 E-Commerce Database Schema (Markdown Version)

This document outlines the table structure used in our SQL practice e-commerce database.

---

## 📦 `users`
Stores registered user information.

| Column             | Data Type      | Constraints               |
|--------------------|----------------|----------------------------|
| `id`               | INT            | PRIMARY KEY, AUTO_INCREMENT |
| `name`             | VARCHAR(255)   | NOT NULL                  |
| `email`            | VARCHAR(255)   | UNIQUE, NOT NULL          |
| `registration_date`| DATETIME       | DEFAULT CURRENT_TIMESTAMP |

---

## 🛍️ `products`
Product catalog details.

| Column      | Data Type      | Constraints               |
|-------------|----------------|----------------------------|
| `id`        | INT            | PRIMARY KEY, AUTO_INCREMENT |
| `name`      | VARCHAR(100)   | NOT NULL                  |
| `category_id`| INT           | FOREIGN KEY → `categories(id)` |
| `price`     | DECIMAL(10,2)  | NOT NULL                  |
| `stock`     | INT            | DEFAULT 0                 |

---

## 🗂️ `categories`
Product category information.

| Column | Data Type     | Constraints               |
|--------|---------------|----------------------------|
| `id`   | INT           | PRIMARY KEY, AUTO_INCREMENT |
| `name` | VARCHAR(100)  | UNIQUE, NOT NULL          |

---

## 📑 `orders`
Order summary table.

| Column         | Data Type      | Constraints               |
|----------------|----------------|----------------------------|
| `id`           | INT            | PRIMARY KEY, AUTO_INCREMENT |
| `user_id`      | INT            | FOREIGN KEY → `users(id)`  |
| `ordered_at`   | DATETIME       | DEFAULT CURRENT_TIMESTAMP |
| `total_amount` | DECIMAL(10,2)  | NOT NULL                  |
| `payment_status` | ENUM(...)   | DEFAULT 'processing'      |

---

## 📦 `order_items`
Details of each product in an order.

| Column     | Data Type      | Constraints               |
|------------|----------------|----------------------------|
| `id`       | INT            | PRIMARY KEY, AUTO_INCREMENT |
| `order_id` | INT            | FOREIGN KEY → `orders(id)` |
| `product_id` | INT          | FOREIGN KEY → `products(id)` |
| `quantity` | INT            | NOT NULL                  |
| `price`    | DECIMAL(10,2)  | NOT NULL                  |

---

## 💳 `payments`
Payment transaction information.

| Column    | Data Type      | Constraints               |
|-----------|----------------|----------------------------|
| `id`      | INT            | PRIMARY KEY, AUTO_INCREMENT |
| `order_id`| INT            | FOREIGN KEY → `orders(id)` |
| `method`  | ENUM(...)      | NOT NULL                  |
| `status`  | ENUM(...)      | NOT NULL                  |
| `paid_at` | DATETIME       |                            |

---

## 🚚 `deliveries`
Delivery status for each order.

| Column             | Data Type      | Constraints               |
|--------------------|----------------|----------------------------|
| `id`               | INT            | PRIMARY KEY, AUTO_INCREMENT |
| `order_id`         | INT            | FOREIGN KEY → `orders(id)` |
| `status`           | ENUM(...)      | DEFAULT 'pending'         |
| `delivery_address` | VARCHAR(255)   | NOT NULL                  |
| `courier_name`     | VARCHAR(100)   |                            |
| `expected_delivery`| DATETIME       |                            |
| `delivered_at`     | DATETIME       |                            |

---

## 📝 `product_reviews`
Reviews and rating for products by users.

| Column        | Data Type      | Constraints               |
|---------------|----------------|----------------------------|
| `id`          | INT            | PRIMARY KEY, AUTO_INCREMENT |
| `product_id`  | INT            | FOREIGN KEY → `products(id)` |
| `user_id`     | INT            | FOREIGN KEY → `users(id)`    |
| `rating`     | INT            | CHECK (1–5)                |
| `reviews`     | VARCHAR(300)   | NOT NULL                  |
| `review_date` | DATETIME       | DEFAULT CURRENT_TIMESTAMP |

"""



# 📘 SQL Basics: Theory Summary

This document summarizes key SQL concepts that were practiced through e-commerce-related problems.

---

## ✅ SELECT Statement

The `SELECT` statement is used to retrieve data from one or more tables.

```sql
SELECT column1, column2 FROM table_name;
```

---

## ✅ WHERE Clause

Used to filter rows based on conditions.

```sql
SELECT * FROM orders WHERE payment_status = 'paid';
```

---

## ✅ ORDER BY

Used to sort the results based on one or more columns.

```sql
SELECT * FROM products ORDER BY price DESC;
```

---

## ✅ DISTINCT

Used to eliminate duplicate values.

```sql
SELECT DISTINCT user_id FROM orders;
```

---

## ✅ JOINs

### INNER JOIN
Returns only matching rows between two tables.

```sql
SELECT o.id, u.name FROM orders o
INNER JOIN users u ON o.user_id = u.id;
```

### LEFT JOIN
Returns all rows from the left table and matching rows from the right table (or NULL if no match).

```sql
SELECT p.name FROM products p
LEFT JOIN order_items oi ON p.id = oi.product_id
WHERE oi.product_id IS NULL;
```

---

## ✅ GROUP BY

Used with aggregate functions to group rows that have the same values.

```sql
SELECT user_id, COUNT(*) FROM orders GROUP BY user_id;
```

---

## ✅ HAVING

Used to filter groups (works with GROUP BY).

```sql
SELECT user_id, COUNT(*) FROM orders
GROUP BY user_id
HAVING COUNT(*) > 3;
```

---

## ✅ Aggregate Functions

- `COUNT(*)`: Total number of rows
- `SUM(column)`: Sum of values
- `AVG(column)`: Average of values
- `MAX(column)`, `MIN(column)`: Highest/lowest values

```sql
SELECT AVG(price) FROM products;
```

---

## ✅ Subqueries

A query nested inside another query.

```sql
SELECT name FROM users
WHERE id IN (
  SELECT user_id FROM orders GROUP BY user_id HAVING COUNT(*) > 3
);
```

---

## ✅ CASE WHEN (Conditional Logic)

```sql
SELECT 
  name,
  CASE 
    WHEN stock = 0 THEN 'Out of Stock'
    ELSE 'In Stock'
  END AS availability
FROM products;
```

---

This summary covers the key SQL clauses and logic patterns used in beginner and intermediate level queries.


# ✅ Advanced Aggregation & Window Functions in SQL

Window functions allow you to perform aggregations **across a set of rows** while still **retaining individual row information**. Unlike `GROUP BY`, window functions don't collapse rows.

---

## 🧠 Key Concepts

| Function | Description |
|----------|-------------|
| `ROW_NUMBER()` | Assigns a unique number to each row within a partition |
| `RANK()` / `DENSE_RANK()` | Ranks rows by a specific order (with or without gaps) |
| `PARTITION BY` | Resets ranking or aggregation for each group |
| `ORDER BY` (inside OVER) | Specifies row order within partition |
| `LAG()` / `LEAD()` | Access previous/next row's value |
| `SUM() OVER` / `AVG() OVER` | Running total / moving average |

---

## 🔍 Use Case: Top 3 Most Expensive Products Per Category

Assuming:
- `products(id, name, category_id, price)`
- `categories(id, name)`

### Step-by-step Query:

```sql
SELECT 
    p.name, 
    c.name AS category_name,
    p.price,
    ROW_NUMBER() OVER (
        PARTITION BY p.category_id
        ORDER BY p.price DESC
    ) AS price_rank
FROM products p
JOIN categories c ON p.category_id = c.id;
```