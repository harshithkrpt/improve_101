# 3Sum
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.

# The output should not contain any duplicate triplets. You may return the output and the triplets in any order.

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]

# Output: [[-1,-1,2],[-1,0,1]]
# Explanation:
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].

# Example 2:

# Input: nums = [0,1,1]

# Output: []
# Explanation: The only possible triplet does not sum up to 0.

# Example 3:

# Input: nums = [0,0,0]

# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.


# My Solution
# Sort the Array 
# loop through each element 
# i + l + r === 0 -> push it to array after sorting 
#  maintain the key of these three elements to avoid duplicates

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sn = sorted(nums)
        memory = {}
        res = []
        for index,num in enumerate(sn):
            l = 0
            r = len(sn) - 1
            while(l < r):
                if sn[l] + sn[r] + num == 0 and l != index and r != index:
                    # Store the Output
                    l_ans = sorted([sn[l], sn[r], num])
                    key = "{} {} {}".format(l_ans[0], l_ans[1], l_ans[2])
                    if key not in memory:
                        memory[key] = True
                        res.append(l_ans)
                    l += 1
                    
                elif sn[l] + sn[r] + num > 0:
                    r -= 1
                else:
                    l += 1
        return res


# Solution by neetcode
# Sort the Array
# loop through each element
# check if previous first element is same then move to next iteration
# IMPORTANT:
# i + l + r === 0 -> push it to array after sorting 
    # if l is same as before go to next element
    # if r is same as before go to previous element
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sn = sorted(nums)
        res = []
        for index,num in enumerate(sn):
            if index > 0 and sn[index-1] == num:
                continue
            l = index + 1
            r = len(sn) - 1
            while(l < r):
                if sn[l] + sn[r] + num == 0:
                    res.append([sn[l], sn[r], num])
                    while l < r and sn[l] == sn[l + 1]:
                        l += 1
                    while l < r and sn[r] == sn[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif sn[l] + sn[r] + num > 0:
                    r -= 1
                else:
                    l += 1
        return res