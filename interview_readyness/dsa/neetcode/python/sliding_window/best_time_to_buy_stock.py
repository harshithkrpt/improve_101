# solution 1
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = 1000000
        maxP = 0

        for p in prices:
            if min_price > p:
                min_price = p
            else:
                maxP = max(maxP, p - min_price)
        
        return maxP



class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        n = len(prices)
        maxP = 0

        while r < n:
            if prices[l] < prices[r]:
                maxP = max(maxP, prices[r] - prices[l])
            else:
                l = r
            r = r + 1
        return maxP