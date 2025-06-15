# ✅ Optimal Algorithm: Monotonic Stack (O(n) Time)
# Approach:
# Use a stack to keep indices of the bars in increasing height order.

# For every bar:

# If it's higher than the bar at stack top, push its index.

# If it’s lower, repeatedly pop from the stack and calculate area:

# Height = height[stack.pop()]

# Width = current index - stack top - 1

# After iterating, repeat for any remaining bars in the stack.


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # pair(index, height)
        maxArea = 0

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > heights[i]:
                index, c_h = stack.pop()
                maxArea = max(maxArea, c_h * (i - index))
                # Start is important as we have to make the previous 
                # extending index as we can calculate the area backwards
                start = index
            stack.append((start, h))
        
        for i,h in stack:
            maxArea = max(maxArea, h * (len(heights)- i))

        return maxArea