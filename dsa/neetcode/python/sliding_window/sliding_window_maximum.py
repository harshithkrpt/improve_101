# You are given an array of integers nums and an integer k. There is a sliding window of size k that starts at the left edge of the array. The window slides one position to the right until it reaches the right edge of the array.

# Return a list that contains the maximum element in the window at each step.

# Monotonically Decreasing Queue

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, r = 0, 0
        output = []
        dqu = collections.deque() #store the index
        while r < len(nums):
            # while top value is less then nums[r] pop
            while dqu and nums[dqu[-1]] < nums[r]:
                dqu.pop()
            # add indexes to the queue
            dqu.append(r)
        
            # now pop the left if the left index is out of bound
            if dqu[0] < l:
                dqu.popleft()

            # only add to ouput if r + 1 >= k
            if r + 1 >= k:
                output.append(nums[dqu[0]])
                l += 1
            r += 1


        return output