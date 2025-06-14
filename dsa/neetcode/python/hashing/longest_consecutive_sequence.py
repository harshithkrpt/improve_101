# https://neetcode.io/problems/longest-consecutive-sequence?list=neetcode150

# Longest Consecutive Sequence
# Solved 
# Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.

# A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.

# You must write an algorithm that runs in O(n) time.

# Example 1:

# Input: nums = [2,20,4,10,3,4,5]

# Output: 4
# Explanation: The longest consecutive sequence is [2, 3, 4, 5].

# Example 2:

# Input: nums = [0,3,2,5,4,6,1,1]

# Output: 7


# Solution -> very is very un intuitive the thing is we have to find all the numbers which are present irrespective of order / duplicate 
# just find the consecutive 
# what we are trying to do is we are maintaining a set of all the numbers
# looping through every number and checking if number - 1 exists iteratively and storing the max value 
# that max value becomes answer

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # hash map for o(1) lookup
        maxi = 0
        set_v = set(nums) 
        for n in nums:
            length = 1
            num_minus_one = n - 1
            while(num_minus_one in set_v):
                num_minus_one -= 1
                length += 1
            maxi = max(length, maxi)
        
        return maxi