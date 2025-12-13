## Most Important Parent Problems 

- 0-1 Knapsack Problem
- Unbounded Knapsack Problem
- Fibonacci Problem
- LCS 
- LIS
- Kadane's Algorithm
- Matrix Chain Multiplication
- DP on trees
- DP on grid
- Misc -> Find out what


- identifying dp problems 
    - it should have a choice 
    - it should be trying to find optimal solution -> min, max, ...
- dp -> recursion + storage
    - memoization approach
    - top down approach

- 0/1 Knapsack Recursive

Ip -> wt[] -> [1,3,4,5]
Ip -> val[] -> [1,4,5,7]
W : 7

```js
function knapSack(wt, val, W, n, memo = {}) {
    const key = `${n}-${W}`
    if(memo[key]) return memo[key];
    if(n == 0 || W == 0) return 0;
    let res;
    if(wt[n-1] <= W) {
        res =  Math.max(val[n-1] + knapSack(wt, val, W - wt[n-1], n - 1), knapSack(wt, val, W, n - 1));
    }
    else {
        res = knapSack(wt, val, W, n - 1);
    }
    memo[key] = res;
    return res;
}
``` 

Your recursive knapsack is the classic, pure-as-snow brute-force version. It’s correct, but it explodes into a combinatorial mess the moment *n* gets frisky. The function is essentially wandering the solution tree like a curious raccoon: endearing, but wildly inefficient.

Here’s what your code is doing, in plain DP-logic:

1. When you look at item `n-1`, you ask:
   “Can I include this fellow?”
2. If yes, explore two universes:
   one where you take it, one where you abandon it.
3. If no, you only explore the sad universe of exclusion.

Everything is right. The missing piece is memoization (storing results), otherwise the same subproblems keep getting recomputed.

To evolve your function from raccoon-brain to something more owl-like, just add a memo table keyed by `(n, W)`.

Here’s the same function with memoization while keeping your structure intact:

```js
function knapSack(wt, val, W, n, memo = {}) {
    const key = `${n}-${W}`;

    if (key in memo) return memo[key];
    if (n === 0 || W === 0) return 0;

    let result;

    if (wt[n - 1] <= W) {
        result = Math.max(
            val[n - 1] + knapSack(wt, val, W - wt[n - 1], n - 1, memo),
            knapSack(wt, val, W, n - 1, memo)
        );
    } else {
        result = knapSack(wt, val, W, n - 1, memo);
    }

    memo[key] = result;
    return result;
}
```

That tiny memo object turns exponential recursion into pseudo-polynomial time.

If you want to travel one more step down the DP rabbit hole, the bottom-up table version is a thing of beauty because you can stare at it and *see* the subproblems being filled.

Let’s put the two versions under a microscope and watch how time behaves when *n* starts misbehaving.

### 1) **Pure recursive (your original code)**

This version explores **every include/exclude possibility** for each item.

For every item, you branch into two calls:

* include the item
* exclude the item

That creates a recursion tree with roughly:

**Time Complexity:**
**O(2ⁿ)**

Why?

* Each of the `n` items has two choices
* Many subproblems like `(n=3, W=10)` are recomputed again and again
* The weight `W` does **not** limit recomputation here

Think of it as brute-force power set exploration.

---

### 2) **Recursive + memoization (Top-Down DP)**

Here, each subproblem is uniquely identified by:

* `n` → number of items considered
* `W` → remaining capacity

How many such states exist?

* `n` ranges from `0 → N`
* `W` ranges from `0 → W`

So total unique states:

**N × W**

Each state is computed once, then cached.

**Time Complexity:**
**O(N × W)**

**Space Complexity:**
**O(N × W)** (memo table + recursion stack)

---

### Side-by-side intuition

| Version        | Time Complexity | Why                                    |
| -------------- | --------------- | -------------------------------------- |
| Pure recursion | **O(2ⁿ)**       | Recomputes same subproblems repeatedly |
| Memoized (DP)  | **O(N × W)**    | Each `(n, W)` solved once              |

---

### Mental model to remember

* **Recursion alone** → “Try all combinations”
* **DP (memo/table)** → “Solve each subproblem once”

This is the single most important leap in dynamic programming:
**stop re-solving the past.**

From here, bottom-up tabulation is just a different way of organizing the same `N × W` work.

Here’s the **bottom-up (iterative) DP** version of the **same 0/1 Knapsack logic** you wrote — no recursion, no stack drama, just a table filling itself with quiet determination.

### Bottom-up idea in one breath

`dp[i][w]` = **maximum value using first `i` items with capacity `w`**

We build the answer from the smallest subproblems upward.

---

### Bottom-up iterative code (JS)

```js
function knapSack(wt, val, W, n) {
    // dp[i][w] → max value using first i items and capacity w
    const dp = Array.from({ length: n + 1 }, () =>
        Array(W + 1).fill(0)
    );

    for (let i = 1; i <= n; i++) {
        for (let w = 1; w <= W; w++) {
            if (wt[i - 1] <= w) {
                dp[i][w] = Math.max(
                    val[i - 1] + dp[i - 1][w - wt[i - 1]],
                    dp[i - 1][w]
                );
            } else {
                dp[i][w] = dp[i - 1][w];
            }
        }
    }

    return dp[n][W];
}
```

---

### Why this is the *same* logic as your recursion

Your recursive choice:

```
take item OR skip item
```

Bottom-up does **the exact same comparison**, just precomputed:

```
dp[i][w] = max(
  value of taking item i,
  value of skipping item i
)
```

No repeated work. No call stack. No exponential explosion.

---

### Time & space (to lock it in memory)

* **Time:** `O(N × W)`
* **Space:** `O(N × W)`

---

### Extra nerd candy 🍬 (space optimized)

If you ever want to flex:

```js
function knapSack(wt, val, W, n) {
    const dp = Array(W + 1).fill(0);

    for (let i = 0; i < n; i++) {
        for (let w = W; w >= wt[i]; w--) {
            dp[w] = Math.max(
                dp[w],
                val[i] + dp[w - wt[i]]
            );
        }
    }

    return dp[W];
}
```

This works because each row only depends on the previous one.

---

You’ve now seen the full evolution path:

**Brute recursion → Memoization → Bottom-up → Space optimized**

That’s basically the hero’s journey of dynamic programming.

Dynamic programming has a small number of *ideas* and an absurd number of costumes. If you master the right set, most interview DP problems stop looking mysterious and start looking repetitive in a comforting way.

Here’s a **curated list of 20 must-solve DP problems**, split cleanly into **1D and 2D DP**. This set is enough to build real intuition, not just pattern memorization.

---

### 1D DP (state depends on previous states)

These train you to think: “What does `dp[i]` mean?”

1. **Fibonacci Number**
   The hello-world of DP: overlapping subproblems + recurrence.

2. **Climbing Stairs**
   Same recurrence as Fibonacci, but teaches problem translation.

3. **House Robber**
   Classic take-or-skip DP.

4. **Maximum Subarray (Kadane’s Algorithm)**
   DP disguised as a greedy one-liner.

5. **Min Cost Climbing Stairs**

6. **Decode Ways**
   Subtle transitions, careful indexing.

7. **Coin Change (minimum coins)**
   Unbounded knapsack in 1D.

8. **Coin Change II (number of ways)**
   Same state, different meaning.

9. **Longest Increasing Subsequence (DP version)**
   Builds DP thinking before binary-search optimization.

10. **Partition Equal Subset Sum**
    1D knapsack optimization mindset.

---

### 2D DP (two changing dimensions)

These force you to define state clearly or crash gloriously.

11. **0/1 Knapsack**
    The keystone. Everything else bows to this.

12. **Subset Sum**
    Knapsack stripped to its skeleton.

13. **Longest Common Subsequence (LCS)**
    The canonical string DP.

14. **Longest Common Substring**
    Similar table, very different transition (resets to zero).

15. **Edit Distance**
    Insert / delete / replace transitions—DP with consequences.

16. **Minimum Path Sum (grid)**
    Grid DP fundamentals.

17. **Unique Paths**
    Combinatorics pretending to be DP.

18. **Target Sum**
    Reduction to subset sum—excellent transformation practice.

19. **Ones and Zeroes**
    2D knapsack with two constraints.

20. **Burst Balloons**
    Interval DP: the final boss of DP thinking.

---

### How to study this list (important)

For **each problem**, force yourself to answer *out loud*:

* What does my DP state represent?
* What choice am I making?
* What information do I need from the past?

If you can explain those three things cleanly, you’re not just solving DP—you’re *thinking* in DP.

This list forms a complete mental toolkit:
1D for sequence decisions,
2D for constraints, comparisons, and grids,
interval DP for when time itself bends.

Once these are solid, medium DP problems start collapsing into familiar shapes instead of feeling like fresh nightmares.
