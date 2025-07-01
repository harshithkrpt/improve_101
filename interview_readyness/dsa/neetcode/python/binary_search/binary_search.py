class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lp = 0
        rp = len(nums) - 1
        while(lp <= rp):
            # get the middle most index
            middle = (rp + lp) // 2
            if(nums[middle] == target):
                return middle
            elif nums[middle] < target:
                lp = middle + 1
            else:
                rp = middle - 1
        return -1