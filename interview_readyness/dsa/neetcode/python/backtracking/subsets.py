from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subsets = []
        def dfs(i):
            if i >= len(nums):
                res.append(subsets.copy())
                return
            
            subsets.append(nums[i])
            dfs(i+1)

            subsets.pop()
            dfs(i+1)
        dfs(0)
        return res
    
class ForLoopSolution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtrack(index, cur_subsets: List[int]):
            res.append(list(cur_subsets))
            for i in range(index, len(nums)):
                cur_subsets.append(nums[i])
                backtrack(i+1, cur_subsets)
                cur_subsets.pop()
        backtrack(0, [])
        return res

class Combinations:
    def subsets(self, nums: List[int], k: int) -> List[List[int]]:
        res = []
        
        def backtrack(index, cur_subsets: List[int]):
            if len(cur_subsets) == k:
                res.append(list(cur_subsets))
                return
            for i in range(index, len(nums)):
                cur_subsets.append(nums[i])
                backtrack(i+1, cur_subsets)
                cur_subsets.pop()
        backtrack(0, [])
        return r