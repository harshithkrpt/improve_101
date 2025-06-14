class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        for num in nums:
            print(num, hashmap)
            if num in hashmap.keys():
                return True
            else:
                hashmap[num] = True
        return False