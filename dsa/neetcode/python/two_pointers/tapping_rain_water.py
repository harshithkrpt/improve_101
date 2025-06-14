# Dynamic Programming Solution
# 🧠 Intuition:
# The water trapped at any index i depends on the shorter of the tallest bars to its left and right.

# The difference between that height and the current bar's height is the water it can trap.

class Solution:
    def trap(self, height: List[int]) -> int:
        max_l = [0] * len(height)
        max_r = [0] * len(height)
        min_l_r = [] * len(height)

        max_p = 0
        for i in range(1, len(height)):
            max_l[i] = max(max_p, height[i-1])
            max_p = max_l[i]
        max_p = 0
        for i in range(len(height) - 2, -1,-1):
            max_r[i] = max(max_p, height[i + 1])
            max_p = max_r[i]

        ans = 0   
        for i in range(len(height)):
           l_ans = min(max_l[i], max_r[i]) - height[i]
           
           if l_ans > 0:
            ans += l_ans 

        return ans


# Two Pointer Solution :
# The idea is:
# Instead of precomputing and storing max_left and max_right arrays, we can compute them on the fly using two pointers (left and right) that move toward each other.
# The key observation:
# Water trapped at position i only depends on the shorter side — because water cannot spill over the taller side.
# So at any point:
# If height[left] < height[right], then the water trapped depends on max_left.
# Else, it depends on max_right.


class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        length = len(height) - 1
        max_l = height[0]
        max_r = height[length]  
        l = 0
        r = length

        while(l < r):
            if max_l <= max_r:
                l += 1
                l_ans =  max_l - height[l] 
                max_l = max(max_l, height[l])
                
                if l_ans > 0:
                    ans += l_ans
            else:
                r -= 1
                l_ans = max_r - height[r] 
                max_r = max(max_r, height[r])
                
                if l_ans > 0:
                    ans += l_ans
        return ans