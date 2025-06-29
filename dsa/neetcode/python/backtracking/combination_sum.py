from typing import List


class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        def backtrack(i, cur , total):
            if total == target:
                res.append(list(cur))
            
            for j in range(i, len(nums)):
                if total + nums[j] > target:
                    return
                cur.append(nums[j])
                backtrack(j, cur, total + nums[j])
                cur.pop()
        backtrack(0,[],0)
        return res