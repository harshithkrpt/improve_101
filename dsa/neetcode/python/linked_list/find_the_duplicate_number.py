# 🐢🪿 Floyd’s Two Pointers Walkthrough
# Phase 1: Find intersection point
# Use two pointers:

# slow = nums[slow]

# fast = nums[nums[fast]]

# They will meet inside the cycle.

# Phase 2: Find the entrance of the cycle
# Reset slow to 0 (or nums[0] if you're skipping index 0).

# Now move both slow and fast one step at a time.

# They will meet at the duplicate number (entrance to the cycle).

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0,0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow1 = 0 
        while True:
            slow = nums[slow]
            slow1 = nums[slow1]

            if slow == slow1:
                return slow
        