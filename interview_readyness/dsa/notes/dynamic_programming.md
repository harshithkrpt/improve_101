# Lesson 1: What is Dynamic Programming?

---

## ✅ Core Concepts

Dynamic Programming (DP) is a technique for solving **optimization** and **combinatorial** problems by breaking them down into simpler, overlapping subproblems, solving each just once, and storing their results.

A problem is suitable for DP if it exhibits:

1. **Overlapping Subproblems**  
   - The problem can be broken down into subproblems that are reused several times.
   - ✅ *Example:* Computing Fibonacci numbers repeatedly calls `fib(n-1)` and `fib(n-2)`.

2. **Optimal Substructure**  
   - The optimal solution to a problem depends on the optimal solutions to its subproblems.
   - ✅ *Example:* The minimum cost to reach a cell depends on the minimum costs of the cells before it.

---

## 🔁 Two DP Strategies

### 🧠 1. Top-Down (Memoization)
- **Approach:** Recursive + Caching
- **What you do:**  
  Cache the results of subproblems in a map or array to avoid recomputation.
- **Use When:** You prefer recursion and want easier-to-read code.

```python
def fib_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]

# print(fib_memo(10))  # Output: 55
```

### 🧱 2. Bottom-Up (Tabulation)
- **Approach:** Iterative
- **What you do:**  
  Solve smaller subproblems first and build the solution iteratively in a table (usually an array).
- **Use When:** You need better performance (no stack overflow risk).

```python
def fib_tab(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

# print(fib_tab(10))  # Output: 55
```

---

## 🧮 Example: Fibonacci Sequence

### ❌ Naive Recursive (Exponential Time)
```python
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
```
- **Time Complexity:** O(2^n)
- **Space Complexity:** O(n) (due to recursion stack)

### ✅ Top-Down (Memoization)
```python
def fib_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]
```
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

### ✅ Bottom-Up (Tabulation)
```python
def fib_tab(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]
```
- **Time Complexity:** O(n)
- **Space Complexity:** O(n) (can be reduced to O(1) with two variables)

---

## 🪜 Example: Climbing Stairs

### Problem:
You can climb 1 or 2 steps at a time. How many ways are there to climb `n` stairs?

### ✅ DP Solution (Bottom-Up)
```python
def climb_stairs(n):
    if n <= 1:
        return 1
    dp = [1] * (n + 1)
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

# print(climb_stairs(5))  # Output: 8
```

---

## 🧠 TL;DR Summary

| Concept         | Top-Down (Memoization)        | Bottom-Up (Tabulation)         |
|----------------|-------------------------------|--------------------------------|
| Approach        | Recursive + Caching           | Iterative                      |
| Memory Usage    | Stack + Cache (O(n))          | DP table (O(n))                |
| Readability     | Simple recursion              | Explicit loop logic            |
| Performance     | Better than naive recursion   | Faster and stack-safe          |

## 🎒 0/1 Knapsack Problem


---

### 📌 Problem Statement

You are given:
- `n` items, each with a **weight `w[i]`** and **value `v[i]`**.
- A **knapsack capacity `W`**.

> **Goal:** Maximize the total value you can fit in the knapsack **without exceeding capacity `W`**, where each item can be **picked only once** (0 or 1 times).

---

### ✅ Constraints

- Either pick an item **or** don't pick it.
- If total weight > capacity, skip that item.
- Solve using **Dynamic Programming**.

---

### 🧠 Recurrence Relation

```
dp[i][w] = max(
   dp[i-1][w],                      # Case 1: don't pick item i
   value[i-1] + dp[i-1][w - weight[i-1]]  # Case 2: pick item i (if it fits)
)
```

---

### 🏗️ DP Matrix (Tabulation)

- `dp[i][j]` = Max value using **first i items** and **capacity j**
- Matrix size: `(n+1) x (W+1)`

---

### 📦 Example

Let’s take 3 items and capacity `W = 4`:

| Item | Weight | Value |
|------|--------|--------|
| 1    |   1    |   1    |
| 2    |   2    |   4    |
| 3    |   3    |   5    |

---

### 📊 DP Matrix Table

| i\w | 0 | 1 | 2 | 3 | 4 |
|------|---|---|---|---|---|
| 0    | 0 | 0 | 0 | 0 | 0 |
| 1    | 0 | 1 | 1 | 1 | 1 |
| 2    | 0 | 1 | 4 | 5 | 5 |
| 3    | 0 | 1 | 4 | 5 | 6 |

🔍 **Explanation:**
- Row 1 (item 1): only item 1 considered.
- Row 2 (items 1,2): try adding item 2 where possible.
- Row 3 (items 1,2,3): pick best option between item 2 and 3.

---

### 🧮 Final Answer

> **Maximum value = `dp[3][4] = 6`**

---

### 💻 Code (Python)

```python
def knapsack(weights, values, W):
    n = len(weights)
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(W + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], values[i-1] + dp[i-1][w - weights[i-1]])
            else:
                dp[i][w] = dp[i-1][w]
    
    return dp[n][W]

# weights = [1, 2, 3]
# values = [1, 4, 5]
# W = 4
# print(knapsack(weights, values, W))  # Output: 6
```

---

### 🧠 Insight

0/1 Knapsack is a **classic example** of applying **bottom-up DP** to handle **inclusion/exclusion** decisions.

---