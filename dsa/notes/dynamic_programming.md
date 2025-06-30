# Lesson 1: What is Dynamic Programming?

## Core Concepts

Dynamic Programming (DP) is a method for solving complex problems by breaking them down into simpler, overlapping subproblems. The results of these subproblems are stored to avoid re-computation.

A problem is suitable for DP if it has:

1.  **Overlapping Subproblems:** The same subproblems are encountered and solved multiple times.
2.  **Optimal Substructure:** The optimal solution to the overall problem can be constructed from the optimal solutions of its subproblems.

## DP Strategies

There are two main ways to implement a DP solution:

### 1. Top-Down (Memoization)
- **Approach:** Recursive.
- **Method:** You write a standard recursive function but add a cache (e.g., a dictionary or array) to store results. Before computing, you check the cache. If the result is there, return it. Otherwise, compute the result, store it in the cache, and then return it.
- **Analogy:** Writing a value on a sticky note to avoid recalculating it later.

### 2. Bottom-Up (Tabulation)
- **Approach:** Iterative (using loops).
- **Method:** You start by solving the smallest possible subproblems and store their results in a table (e.g., an array). You then use these results to progressively build solutions for larger subproblems until you solve the original problem.
- **Analogy:** Building a Lego tower from the base blocks up to the top.


## Fibonacci 

- normal recusrive solution

```python
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
```

```python
def fib_memo(n, memo={}):
  if n in memo:
    return memo[n]

  # Base cases for the recursion
  if n <= 1:
    return n
  memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
  return memo[n]

# Example call (should print 55)
# print(fib_memo(10))
```