class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_num = 0
        min_num = 1
        for num in piles:
            max_num = max(max_num, num)
        res = max_num
        while min_num <= max_num:
            middle = (max_num + min_num) // 2
            total = 0
            for n in piles:
              total = total + math.ceil(n/middle)
            if total <= h:
                res = min(res, middle)
                max_num = middle - 1
            else:
                min_num = middle + 1
                
        return res
            