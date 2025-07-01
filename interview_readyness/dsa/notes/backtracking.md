
# 🧠 Backtracking: Mastery Notes

## The Method: Recursion
Backtracking is built upon **recursive exploration**. It tries all possible solutions and *backtracks* once it realizes a path won't work.

---

## The Map: Decision Tree
Visualize backtracking as a **decision tree** where:
- Each level represents a decision.
- Each node branches into all valid options.
- You explore each branch **depth-first**.

Example: Generating subsets of `[1, 2]`

```
            []
           /  \
         [1]  []
        /   \
     [1,2]  [2]
```

---

## The Destination: Base Case
The **base case** defines when to:
- Stop recursion.
- Add the current path/solution to the result.

```python
# Template
def backtrack(path, choices):
    if base_case(path, choices):
        res.append(path[:])
        return
```

---

## Backtracking Template

```python
def backtrack(path, choices):
    if base_case(path, choices):
        res.append(path[:])
        return

    for i in range(len(choices)):
        # Choose
        path.append(choices[i])

        # Explore
        backtrack(path, updated_choices)

        # Un-choose (Backtrack)
        path.pop()
```

---

## When to Use Backtracking

✅ All permutations  
✅ All combinations / subsets  
✅ Solve puzzles (Sudoku, N-Queens)  
✅ Find all paths (maze, grid problems)  
✅ Partitioning problems

---

## Key Concepts

- **Choose, Explore, Unchoose** (core idea)
- **State restoration** is crucial (undoing the choice).
- Avoid side-effects across recursion levels (use `.pop()` or copy lists).
- Prune paths early (e.g., if invalid state or no solution possible).

---

## Patterns to Master

1. **Permutations**
2. **Combinations**
3. **Subsets (Power set)**
4. **N-Queens**
5. **Palindrome Partitioning**
6. **Sudoku Solver**
7. **Word Search (DFS + Backtracking)**
8. **Graph Coloring / Safe Paths**

---

## Debugging Tips

- Log your path before and after each recursive call.
- Watch for:
  - Incorrect base cases
  - Not restoring state properly
  - Not copying list when needed

```python
print("Before:", path)
backtrack(path)
print("After :", path)
```

---

## Mantra
> "The method is recursion,  
> the map is a decision tree,  
> the destination is the base case,  
> the journey requires pruning and restoration."

---

## Bonus: Time Complexity (Rough Estimation)

- **Subsets:** O(2^n)
- **Permutations:** O(n * n!)
- **N-Queens:** O(n!)
- **Sudoku Solver:** O(9^m) where m = number of empty cells

---

## Daily Practice (Suggested)

| Day | Focus | Example Problems |
|-----|-------|------------------|
| 1   | Subsets | Leetcode 78 |
| 2   | Combinations | Leetcode 77 |
| 3   | Permutations | Leetcode 46, 47 |
| 4   | Palindromic Partitioning | Leetcode 131 |
| 5   | N-Queens | Leetcode 51 |
| 6   | Sudoku Solver | Leetcode 37 |
| 7   | Word Search | Leetcode 79 |

---


## Combinations 

```python
def combinations(nums):
  res = []
  def backtrack(i, current_subset):
    res.append(list(current_subset))

    for j in range(i, len(nums)):
      current_subset.append(nums[i])
      backtrack(i+1, current_subset)
      current_subset.pop()
  backtrack(0, [])
  return res
```

## Permutations

```python
def permutations(nums):
  res = []
  visited = [False] * len(nums)
  def backtrack(subset):
    if len(subset) == len(nums):
      res.append(list(subset))
      return
    for i in range(len(nums)):
      # skip
      if visited[i]:
        continue
      
      visited[i] = True
      subset.append(nums[i])
      backtrack(subset)
      visited[i] = False
      subset.pop()
  backtrack([])
  return res
```