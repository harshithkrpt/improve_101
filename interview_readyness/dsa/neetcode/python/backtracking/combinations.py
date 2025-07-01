from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i + 1 for i in range(n)]
        res = []
        def backtracking(index, current_subset: List[int]):
            if len(current_subset) == k:
                res.append(list(current_subset))
                return
            # explore
            for i in range(index, n):
                current_subset.append(nums[i])
                backtracking(i+1, current_subset)
                current_subset.pop()
        backtracking(0, [])
        return res