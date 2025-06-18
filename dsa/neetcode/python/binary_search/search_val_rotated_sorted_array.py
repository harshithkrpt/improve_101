class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            # find the middle element
            m = (l + r) // 2
            if nums[m] == target:
                return m
            
            # here the important concept is to master the spliting of left sorted array and right sorted array and after that 
            # left sorted : target is less than left most element then it will be right or target is greater then middle it will be right else left
            # right sorted: target is greater than right most element or target is less than middle most element it will be left else right
            if nums[l] <= nums[m]:
                # check for position to moved based on 
                if target < nums[l] or target > nums[m]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if target > nums[r] or target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
        return -1