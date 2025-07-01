# <!-- Container With Most Water
# Solved 
# You are given an integer array heights where heights[i] represents the height of the 
# two bars to form a container. Return the maximum amount of water a container can store.

# Example 1:

# Input: height = [1,7,2,5,4,7,3,6]

# Output: 36

#  -->

# Start with two pointers — one at the beginning and one at the end.

# Calculate area.

# Move the pointer pointing to the shorter height (to possibly get a taller one).

# Keep track of the max area.



class Solution:
    def maxArea(self, h: List[int]) -> int:
        maximum = 0
        l = 0
        r = len(h) - 1

        while(l < r):
            maximum = max(((r - l) * min(h[r],h[l])), maximum)
            if h[l] >= h[r]:
                r -= 1
            else:
                l += 1
        
        return maximum