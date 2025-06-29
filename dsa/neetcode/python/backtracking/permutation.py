from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = [False] * len(nums)
        def backtrack(cur):
            if len(cur) == len(nums):
                res.append(list(cur))
                return
            
            for i in range(len(nums)):
                if visited[i]:
                    continue
                visited[i] = True
                cur.append(nums[i])
                backtrack(cur)
                visited[i] = False
                cur.pop()
        backtrack([])
        return res