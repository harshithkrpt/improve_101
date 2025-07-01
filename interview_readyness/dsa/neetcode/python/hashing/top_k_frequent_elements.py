# We can use bucket sort
# We can use Hashing based approach
# Idea:  
# Use Bucket sort
# add the repeated items in the key and value array of items repeated that many times
# size of the the bucket sort array will be the number of elements or of size (n) as even if all the items are unique w
# it would need any more space


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bk_sort = [None] * len(nums)
        hashed = {}
        for n in nums:
            hashed[n] = 1 + hashed.get(n, 0)
        
        for number,count in hashed.items():
            
            if bk_sort[count - 1] is not None:
                if number not in bk_sort[count -1]:
                    bk_sort[count - 1].append(number)
            else:
                bk_sort[count - 1] = [number]

        res = []
        
        for n in range(len(nums)- 1, -1 ,-1):
            if bk_sort[n] is not None:
                l = len(bk_sort[n])
                for item in range(l):
                    res.append(bk_sort[n][item])

        return res[0:k]


