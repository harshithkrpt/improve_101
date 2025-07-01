# ✅ Algorithm (Using Set and Sliding Window):
# Initialize a set() to store characters in the current window.
# Use two pointers left and right to form a window.
# Iterate right from 0 to n - 1:
# If s[right] is not in the set, add it, update the max length.
# If s[right] is in the set, remove characters from the left until s[right] is not in the set.
# Return the max length.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        maxC = 0
        setC = set()
        for r in range(len(s)):
            # Check duplicates
            while s[r] in setC:
                setC.remove(s[l])
                l += 1
            maxC = max(maxC, r - l + 1)
        return maxC