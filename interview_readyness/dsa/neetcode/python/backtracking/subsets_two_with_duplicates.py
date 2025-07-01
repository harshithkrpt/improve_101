from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def backtrack(index, cur):
            res.append(list(cur))
            for i in range(index, len(nums)):
                if i > index and nums[i-1] == nums[i]:
                    continue
                else:
                    cur.append(nums[i])
                    backtrack(i + 1, cur)
                    cur.pop()
        backtrack(0, [])
        return res