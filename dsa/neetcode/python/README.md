
# 🔁 Problem: Contains Duplicate

Given an integer array `nums`, return `true` if any value appears **at least twice**, and `false` if every element is **distinct**.

---

## ✅ Algorithm (HashSet Approach)

1. Initialize an empty set `seen`.
2. Iterate through each number `num` in `nums`:
   - If `num` is already in `seen`, return `True` (duplicate found).
   - Otherwise, add `num` to `seen`.
3. If loop completes, return `False` (no duplicates).

**Time Complexity:** O(n)  
**Space Complexity:** O(n)

---

## 🐍 Python Code

```python
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
```

---

## 🧪 Example

```python
sol = Solution()
print(sol.containsDuplicate([1, 2, 3, 4]))     # Output: False
print(sol.containsDuplicate([1, 2, 3, 1]))     # Output: True
```



# 🔁 Problem: Valid Anagram

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

---

## ✅ Algorithm (Hash Map Approach)

1. If lengths of `s` and `t` are not equal, return `False`.
2. Create two dictionaries (hash maps) to count characters in both strings.
3. Compare both dictionaries:
   - If they are equal, return `True`.
   - Otherwise, return `False`.

**Time Complexity:** O(n)  
**Space Complexity:** O(n)

---

## 🐍 Python Code

```python
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
```

---

## 🧪 Example

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}

        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        for ch in t:
            if ch not in count or count[ch] == 0:
                return False
            count[ch] -= 1

        return True

```

# 🧮 Two Sum Problem

## 📘 Problem Statement

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to the target.

You may assume that each input would have **exactly one solution**, and you may not use the same element twice.

You can return the answer in any order.

---

## ✅ Algorithm

1. Initialize an empty dictionary `seen`.
2. Iterate over the list using index and value.
3. For each value, compute the complement (`target - value`).
4. If the complement is already in the dictionary, return the indices.
5. Otherwise, store the value and its index in the dictionary.
6. If no pair is found, return an empty list.

---

## 🐍 Python Code

```python
def twoSum(nums, target):
    seen = {}
    for index, value in enumerate(nums):
        complement = target - value
        if complement in seen:
            return [seen[complement], index]
        seen[value] = index
    return []
```

```python
nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))  # Output: [0, 1]

```

# 🧠 Group Anagrams - Using 26-Length Character Count Array

## ✅ Approach: HashMap with Character Frequency Array Key

### 🚀 Intuition
- Anagrams have the **same frequency of each character**.
- Instead of sorting, we can count the frequency of each character in the word using a fixed-size array of length 26.
- Use the tuple of this array as the key in a dictionary.

---

## 🧾 Python Code (No External Libraries)
```python
def groupAnagrams(strs):
    from collections import defaultdict
    
    group_map = defaultdict(list)

    for word in strs:
        # Initialize count array for 26 lowercase letters
        count = [0] * 26
        for char in word:
            count[ord(char) - ord('a')] += 1
        
        # Use tuple of counts as key
        group_map[tuple(count)].append(word)

    return list(group_map.values())

# 🔍 Example usage:
input_strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(input_strs))
```

---

## 🧠 Time & Space Complexity

- **Time Complexity:**  
  \( O(N \cdot K) \)  
  where:
  - \( N \) is the number of strings,
  - \( K \) is the maximum length of a string (26 operations max per word).

- **Space Complexity:**  
  \( O(N \cdot K) \)  
  for storing the groups and count arrays.

### ✅ Advantage Over Sorting Method:
- Avoids sorting → faster especially for long strings.
- Still easy to implement and hashable via tuple.


# 🔝 Top K Frequent Elements - Algorithm and Python Code

## 📌 Problem Statement
Given an integer array `nums` and an integer `k`, return the `k` most frequent elements.  
You may return the answer in **any order**.

### 🧪 Example:
```
Input: nums = [1,1,1,2,2,3], k = 2  
Output: [1,2]
```

---

## ✅ Approach: HashMap + Bucket Sort (Optimal)

### 🚀 Intuition
- Count frequencies of all elements.
- Use a **bucket sort** style list where the index represents the frequency.
- Traverse buckets from high to low frequency to collect top `k` elements.

---

## 🧮 Steps
1. Count frequency of each number using a dictionary.
2. Create a list of empty lists, indexed from `0` to `len(nums)` (since max frequency ≤ len(nums)).
3. Append each number to the bucket at the index equal to its frequency.
4. Traverse the bucket list in reverse order and collect elements until you have `k` of them.

---

## 🧾 Python Code (No External Libraries)
```python
def topKFrequent(nums, k):
    # Step 1: Count frequency
    freq_map = {}
    for num in nums:
        freq_map[num] = 1 + freq_map.get(num, 0)

    # Step 2: Bucket sort based on frequency
    bucket = [[] for _ in range(len(nums) + 1)]
    for num, freq in freq_map.items():
        bucket[freq].append(num)

    # Step 3: Gather top k frequent elements
    res = []
    for freq in range(len(bucket) - 1, 0, -1):
        for num in bucket[freq]:
            res.append(num)
            if len(res) == k:
                return res
```

---

## 🧠 Time & Space Complexity

- **Time Complexity:**  
  \( O(N) \)  
  - Building frequency map: O(N)  
  - Bucket sort: O(N)  
  - Gathering result: O(N)

- **Space Complexity:**  
  \( O(N) \)  
  - For the frequency map and bucket list

---

## 🧠 Alternate Approach: Min-Heap (If `k` ≪ N)

- Build a frequency map
- Push (freq, num) into a **min-heap**
- If heap size > k, pop the smallest
- Return numbers from heap


# 🔐 Encode and Decode Strings - Algorithm and Python Code

## 📌 Problem Statement
Design an algorithm to **encode** a list of strings into a single string, so that it can be **decoded** back to the original list.

You need to implement two functions:

- `encode(strs: List[str]) -> str`
- `decode(s: str) -> List[str]`

### 🧪 Example:
```
Input: ["lint", "code", "love", "you"]
Encoded: "4#lint4#code4#love3#you"
Decoded Output: ["lint", "code", "love", "you"]
```

---

## ✅ Approach: Length Prefix with Delimiter

### 🚀 Intuition
- To differentiate strings, **prefix each string with its length** followed by a special delimiter (e.g., `#`).
- During decoding, read the length, skip the delimiter, and extract the exact number of characters.

---

## 🧮 Steps

### 🔁 Encode
1. For each string `s`, convert it to `len(s) + '#' + s`
2. Join all encoded strings into a single string

### 🔁 Decode
1. Read characters until you find `#` → this gives the length of the next string
2. Use the length to extract the string
3. Repeat until end of the input string

---

## 🧾 Python Code
```python
class Codec:
    def encode(self, strs):
        """Encodes a list of strings to a single string."""
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded

    def decode(self, s):
        """Decodes a single string to a list of strings."""
        res = []
        i = 0
        while i < len(s):
            # Find delimiter to extract length
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j+1:j+1+length])
            i = j + 1 + length
        return res

# 🔍 Example usage:
codec = Codec()
original = ["lint", "code", "love", "you"]
encoded = codec.encode(original)
decoded = codec.decode(encoded)
print("Encoded:", encoded)
print("Decoded:", decoded)
```

---

## 🧠 Time & Space Complexity

- **Encode Time:** \( O(N) \) — where \( N \) is the total number of characters in all strings
- **Decode Time:** \( O(N) \)
- **Space:** \( O(N) \) — for the output string or list

---

## ✅ Notes
- This method handles any character inside the strings (even `#`), because length is used to determine where each string ends.
- Robust and avoids issues from special characters.

# ✖️ Product of Array Except Self - Algorithm and Python Code

## 📌 Problem Statement
Given an integer array `nums`, return an array `output` such that:

```
output[i] = product of all elements in nums except nums[i]
```

**Constraints:**
- Solve in **O(n)** time
- **Do not use division**

---

## ✅ Approach: Prefix and Suffix Product Arrays (O(n) Time, No Division)

### 🚀 Intuition
- To find product of all elements except `nums[i]`, we can multiply:
  - Product of all elements **before** `i` (prefix)
  - Product of all elements **after** `i` (suffix)

Instead of using extra space, we can compute:
1. **Left products** in one pass and store in `res`.
2. Multiply with **right products** in a second pass.

---

## 🧮 Steps
1. Initialize result array `res` with all 1s.
2. In the first pass (left to right):
   - For each index `i`, set `res[i] = res[i-1] * nums[i-1]`
3. In the second pass (right to left):
   - Use a variable `R` to hold product to the right of index `i`
   - Update `res[i] = res[i] * R`, then update `R *= nums[i]`

---

## 🧾 Python Code
```python
def productExceptSelf(nums):
    n = len(nums)
    res = [1] * n

    # Left product pass
    for i in range(1, n):
        res[i] = res[i - 1] * nums[i - 1]

    # Right product pass
    R = 1
    for i in range(n - 1, -1, -1):
        res[i] = res[i] * R
        R *= nums[i]

    return res

# 🔍 Example usage:
nums = [1, 2, 3, 4]
print(productExceptSelf(nums))  # Output: [24, 12, 8, 6]
```

---

## 🧠 Time & Space Complexity

- **Time Complexity:**  
  \( O(n) \) — Two linear passes over the array

- **Space Complexity:**  
  - \( O(1) \) extra space (output array not counted as extra)

---

## ✅ Notes

- This approach **avoids division**, works efficiently for negative numbers and zeros.
- Handles arrays with zeros correctly without special conditions.

# ✅ Valid Sudoku - Algorithm and Python Code

## 📌 Problem Statement
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated **according to Sudoku rules**:

1. Each row must contain the digits `1-9` **without repetition**.
2. Each column must contain the digits `1-9` **without repetition**.
3. Each of the nine `3x3` sub-boxes must contain the digits `1-9` **without repetition**.

### 🔎 Notes
- The board may contain `'.'` for empty cells.
- You only need to check **validity**, not whether it can be solved.

---

## 🧮 Steps
1. Create 3 sets for:
   - Rows: `rows[9]`
   - Columns: `cols[9]`
   - Boxes: `boxes[9]` → where box index = `(r // 3) * 3 + (c // 3)`
2. Traverse each cell `(r, c)` in the board.
3. If the cell is not `.`, check if the digit is already in the corresponding row, column, or box set.
4. If yes, return `False`.
5. Otherwise, add it to all 3 sets.
6. Return `True` if no violations found.

---

## 🧾 Python Code
```python
def isValidSudoku(board):
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]

    for r in range(9):
        for c in range(9):
            val = board[r][c]
            if val == ".":
                continue

            # Check row
            if val in rows[r]:
                return False
            rows[r].add(val)

            # Check column
            if val in cols[c]:
                return False
            cols[c].add(val)

            # Check box
            box_index = (r // 3) * 3 + (c // 3)
            if val in boxes[box_index]:
                return False
            boxes[box_index].add(val)

    return True

# 🔍 Example usage:
board = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
print(isValidSudoku(board))  # Output: True
```

---

## 🧠 Time & Space Complexity

- **Time Complexity:**  
  \( O(1) \)  
  — Fixed 9x9 grid

- **Space Complexity:**  
  \( O(1) \)  
  — 3 arrays of size 9 × at most 9 elements = constant space

---

## ✅ Notes

- This solution ensures that all digits are unique per row, column, and sub-box.
- Does **not** require solving the board.
- Efficient and readable using sets for quick lookup.


# Longest Consecutive Sequence

## ❓ Problem
Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in `O(n)` time.

---

## ✅ Example
**Input:** `nums = [100, 4, 200, 1, 3, 2]`  
**Output:** `4`  
**Explanation:** The longest consecutive sequence is `[1, 2, 3, 4]`.

---

## 💡 Algorithm

1. Put all the numbers in a `set` for O(1) lookups.
2. Iterate through each number in the set.
3. For each number `num`, check if `num - 1` exists in the set.
   - If it **does**, it's not the start of a sequence, so skip.
   - If it **doesn't**, it might be the start of a sequence.
4. Count the length of the sequence starting from `num` by checking consecutive numbers (`num + 1`, `num + 2`, ...).
5. Keep track of the maximum length found.

**Time Complexity:** `O(n)`  
**Space Complexity:** `O(n)`

---

## 🧠 Intuition

Instead of sorting (which takes O(n log n)), we use a set for constant-time lookups and only expand sequences from potential starts, avoiding unnecessary work.

---

## 🧾 Code (Python)

```python
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        num_set = set(nums)
        longest = 0
        
        for num in num_set:
            # only try to build a sequence from start of a sequence
            if num - 1 not in num_set:
                current = num
                streak = 1
                
                while current + 1 in num_set:
                    current += 1
                    streak += 1
                
                longest = max(longest, streak)
        
        return longest
```

# ✅ Valid Palindrome

## 📘 Problem
Given a string `s`, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

---

## 🔍 Algorithm

1. Remove all non-alphanumeric characters from the string.
2. Convert the cleaned string to lowercase.
3. Check if the cleaned string is equal to its reverse.

---

## ✅ Python Code (Simple Version)

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ''
        for ch in s:
            if ch.isalnum():
                cleaned += ch.lower()
        return cleaned == cleaned[::-1]
```


## Optimized version

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True

```

# Two Sum II - Input Array Is Sorted

## Problem
Given a **1-indexed** array of integers `numbers` that is already **sorted in non-decreasing order**, find two numbers such that they add up to a specific target number. Return the indices of the two numbers (1-indexed) as an integer array `answer = [index1, index2]` of length 2.

You may assume that each input would have **exactly one solution** and you may not use the same element twice.

You must solve the problem using only constant extra space.

### Example
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2.


---

## Algorithm (Two-Pointer)

1. Initialize two pointers: `left` at index 0 and `right` at the last index.
2. While `left < right`:
   - Calculate the sum of `numbers[left] + numbers[right]`.
   - If the sum equals the target, return `[left + 1, right + 1]`.
   - If the sum is less than the target, increment `left`.
   - If the sum is greater than the target, decrement `right`.

---

## Python Code

```python
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            curr_sum = numbers[left] + numbers[right]
            if curr_sum == target:
                return [left + 1, right + 1]  # 1-indexed
            elif curr_sum < target:
                left += 1
            else:
                right -= 1
```

# 3 Sum

## Problem Statement
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

## Intuition
We sort the array and fix one element. Then, we use the two-pointer technique to find pairs that sum up to the negative of the fixed element. This avoids duplicates and improves performance compared to a brute-force O(n^3) approach.

## Code
```python
def threeSum(nums):
    nums.sort()
    res = []
    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        l, r = i+1, len(nums)-1
        while l < r:
            total = nums[i] + nums[l] + nums[r]
            if total < 0:
                l += 1
            elif total > 0:
                r -= 1
            else:
                res.append([nums[i], nums[l], nums[r]])
                while l < r and nums[l] == nums[l+1]:
                    l += 1
                while l < r and nums[r] == nums[r-1]:
                    r -= 1
                l += 1
                r -= 1
    return res
```

# Container With Most Water

## Problem Statement
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]). Find two lines that together with the x-axis form a container, such that the container contains the most water. Return the maximum amount of water a container can store.

## Intuition
We use two pointers at the start and end of the array. The idea is to move the pointer with the smaller height inward, because the height of the container is limited by the shorter line. This gives an optimal O(n) solution.

## Code
```python
def maxArea(height):
    left, right = 0, len(height) - 1
    max_area = 0
    while left < right:
        width = right - left
        max_area = max(max_area, min(height[left], height[right]) * width)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area
```

# Trapping Rain Water

## Problem Statement
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

## Intuition
We precompute the maximum height to the left and right of each bar. Then for each position, the water trapped is the minimum of the left and right max minus the current height. This gives an O(n) time and space solution.

## Code
```python
def trap(height):
    if not height:
        return 0
    n = len(height)
    left_max = [0]*n
    right_max = [0]*n
    left_max[0] = height[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i-1], height[i])
    right_max[-1] = height[-1]
    for i in range(n-2, -1, -1):
        right_max[i] = max(right_max[i+1], height[i])
    trapped = 0
    for i in range(n):
        trapped += min(left_max[i], right_max[i]) - height[i]
    return trapped
```

 Optimized Intuition: 

Use two pointers (left and right) starting from both ends.

Keep track of left_max and right_max seen so far.

At every step, compute the water that can be trapped at the current position by comparing left_max and right_max.

```py
def trap(height):
    left, right = 0, len(height) - 1
    left_max = right_max = 0
    trapped_water = 0

    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                trapped_water += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                trapped_water += right_max - height[right]
            right -= 1

    return trapped_water

```