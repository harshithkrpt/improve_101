# https://neetcode.io/problems/products-of-array-discluding-self?list=blind75
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forward_p = []
        backward_p = []

        if len(nums) == 0:
            return []

        last_mul = 1
        for n in nums:
            forward_p.append(last_mul)
            last_mul = last_mul * n

        last_mul = 1
        for n in nums[::-1]:
            backward_p.append(last_mul)
            last_mul = last_mul * n
        backward_p = backward_p[::-1]

        res = []
        for n in range(len(nums)):
            res.append(forward_p[n] * backward_p[n])
        return res
