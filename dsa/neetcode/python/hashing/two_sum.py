from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        idx = []
        for index, num in enumerate(nums):
            dictionary[num] = index
        
        for index, num in enumerate(nums):
            other = target - num
            if other in dictionary and dictionary[other] is not index:
                idx = [dictionary[other], index]
            
        return sorted(idx)