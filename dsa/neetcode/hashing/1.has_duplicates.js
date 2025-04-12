/*
    Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

    Example 1:

    Input: nums = [1, 2, 3, 3]

    Output: true


    Example 2:

    Input: nums = [1, 2, 3, 4]

    Output: false
*/

class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    constructor() {
        this.numberDuplication = {
        };
    }

    hasDuplicate(nums) {
        return nums.filter(num => {
            if(this.numberDuplication[num]) {
               return true;
            }
            else {
               this.numberDuplication[num] = 1;
            }
        }).length > 0;
    }
}

module.exports = Solution;