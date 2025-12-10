
- contains duplicates

```js
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    let hashMap = {};

    for(let i=0;i<nums.length;i++) {
        if(hashMap[nums[i]]) {
            return true;
        }

        hashMap[nums[i]] = 1;
    }

    return false;
};
```


- is valid anagram

```js
/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    const hashMap = {};

    for (let i=0; i < s.length; i++) {
        if(hashMap[s[i]]) {
            hashMap[s[i]]++;
        }
        else {
            hashMap[s[i]] = 1;
        }
    }

    for (let i=0; i < t.length; i++) {
        if(hashMap[t[i]]) {
            hashMap[t[i]]--;
        }
        else {
            return false;
        }
    };
    
    return Object.values(hashMap).filter(v => v > 0).length ? false : true; 
};
```


- two sum

```js
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let hashMap = {};

    for(let i=0;i<nums.length;i++) {
        const remaining = target - nums[i];
        
        if(hashMap[remaining] !== undefined) {
            return [hashMap[remaining], i]
        }

        hashMap[nums[i]] = i;
    }


};
```


- grouped anagrams

```js
/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    // basically maintain the grouped anagram keys
    const hashMapOfGroupedAnagram = {};

    for(let i=0;i<strs.length;i++) {
        let arr = [];
        for(let i=0;i<26;i++) {
            arr.push(0);
        }
       
        for(let j=0;j<strs[i].length;j++) {
            let s = strs[i];
            const index = s.charAt(j).charCodeAt() - 'a'.charCodeAt();
            arr[index] = arr[index] + 1;
        }
       let key = arr.join(",");
        
        if(hashMapOfGroupedAnagram[key]) {
            hashMapOfGroupedAnagram[key].push(strs[i]);
        }
        else {
            hashMapOfGroupedAnagram[key] = [strs[i]];
        }
    }

    


    return Object.values(hashMapOfGroupedAnagram);
};
```


- top k frequent elements

```js
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {
    const freqOfEachNumber = {};
    if (nums.length == 0) return [];
    for(let i=0;i<nums.length;i++) {
        if(freqOfEachNumber[nums[i]]) {
            freqOfEachNumber[nums[i]]++
        }
        else {
            freqOfEachNumber[nums[i]] = 1;
        }
    }

    // maintain the Array with 
    let array = new Array(nums.length + 1);
    
    Object.keys(freqOfEachNumber).forEach(k => {
        if(array[freqOfEachNumber[k]]) {
            array[freqOfEachNumber[k]].push(Number(k));
        }
        else {
            array[freqOfEachNumber[k]] = [Number(k)];
        }
     });

    let res = [];

    for(let i=nums.length;i>=0;i--) {
        if(Array.isArray(array[i])) {
            res = [...res, ...array[i]];
        }

        if(res.length >= k) {
            break;
        }
    }

    return res.slice(0, k);
};
```

- encode & decode strings

```js
class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs) {
        let str = "";
        for(let i=0;i<strs.length;i++) {
            str += `${strs[i].length}#${strs[i]}`;
        }
       
        return str;
    }

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str) {
        let res = [];
        let i=0;
        while(i < str.length - 1) {
            // find the number till we get hash
            let n = "";
            let j=i;
            while(str[j] != "#") {
                n += str[j];
                j++;
            }
            n = Number(n);
            res.push(str.slice(j + 1, j + 1 + n));
            i = j + n + 1;
        }
        return res;
    }
}
```

- multipy of numbers except self


```js
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
   let resultArray = new Array(nums.length).fill(1);
   let tempMultiplication = 1;
   for(let i=0;i<nums.length;i++) {
        resultArray[i] = tempMultiplication;
        tempMultiplication *= nums[i];
   }

    tempMultiplication = 1;
    for(let i=nums.length - 1;i>=0;i--) {
        resultArray[i] *= tempMultiplication;
        tempMultiplication *= nums[i];
    }


   return resultArray;
};
```

- valid sudoko

```js
/**
 * @param {character[][]} board
 * @return {boolean}
 */
var isValidSudoku = function(board) {
const rows = Array.from({ length: 9 }, () => {return {}});
  const cols = Array.from({ length: 9 }, () => {return {}});
  const boxes = Array.from({ length: 9 }, () => {return {}});

    for(let i=0;i<9;i++) {
        for(let j=0;j<9;j++) {
            if(board[i][j] == '.') {
                continue;
            }

            if(rows[i][board[i][j]]) return false;
            rows[i][board[i][j]] = true;

            if(cols[j][board[i][j]]) return false;
            cols[j][board[i][j]] = true;
            
    
            let boxNumber = Math.floor(i/3) * 3 + Math.floor(j / 3); 
            if(boxes[boxNumber][board[i][j]]) {
                return false;
            }
            boxes[boxNumber][board[i][j]] = true;
        }
    }

    return true;
};
```

- longest consecutive sequence

```js
/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function(nums) {
    let set = new Set(nums);

    let max = 0;
    for(let n of set) {
        // find the starting number
        let prev = n - 1;
        if(set.has(prev)) {
            continue;
        }
        
        // else case calculate totoal
        let num = n;
        let count = 0
        while(set.has(n)) {
            n++;
            count++;
        }
        max = Math.max(max, count);
    }

    return max;
};
```

- is valid palindrome

```js
/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {

    const isAlphaChar = (c) => {
        return (
            (c >= 'A' && c <= 'Z') ||
            (c >= 'a' && c <= 'z') ||
            (c >= '0' && c <= '9')
        );
    }

    let lower = s.toLowerCase();
    let i=0,j=lower.length-1;

    while(i < j) {
        let canCompare = true;
        if(!isAlphaChar(lower[i])) {
            i++;
            canCompare = false;
        }
        if(!isAlphaChar(lower[j])) {
            j--;
            canCompare = false;
        }
        if(canCompare) {
            if(lower[i] !== lower[j]) {
                 return false;
            }
            else {
                i++;
                j--;
            }
        }
     }

     return true;
};
```


- two sum if the input is sorted

```js
/**
 * @param {number[]} numbers
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(numbers, target) {
    let l=0,r=numbers.length-1;  
    while(l < r) {
        if(numbers[l] + numbers[r] > target) {
            r--;
        }
        else if(numbers[r] + numbers[l] < target) {
            l++;
        }
        else {
            return [l+1, r+1];
        }
     }
};
```

- three sum 

```js
/**
 * @param {number[]} nums
 * @return {number[][]}
 */

var threeSum = function(nums) {
    let sNums = nums.slice().sort((a,b) => a - b);
    const result = [];
    for(let i=0;i<sNums.length - 2;i++) {
        if(i > 0 && sNums[i] == sNums[i-1]) {
            continue;
        }

        // now check the next items 
        let j = i + 1;
        let k = sNums.length - 1;
        while(j < k) {
            if(sNums[i] + sNums[j] + sNums[k] > 0) {
                k--;
            }
            else if(sNums[i] + sNums[j] + sNums[k] < 0) {
                j++;
            }
            else {
                result.push([sNums[i], sNums[j], sNums[k]]);
                while(j < k && sNums[j] === sNums[j+1]) {
                    j++;
                }
                while(j < k && sNums[k] === sNums[k-1]) {
                    k--;
                }
                j++;
                k--;
            }
        }   
    }

    return result;
};
```

- container with maxmmum water

```js
/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
    let res = 0;
    let l = 0, r = height.length -1;
    while(l < r) {
        res = Math.max(res, (r - l) * Math.min(height[l], height[r]))
        if(height[l] < height[r]) {
            l++;
        }
        else {
            r--;
        }
    }
    return res;
};
```


- kadane algorithm (Maximum Subarray sum ) uses (Greedy + Dynamic Programming)

```js
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {
    let maxAns = nums[0];
    let curMax = nums[0];

    for(let i=1;i<nums.length;i++) {
        curMax = Math.max(nums[i], nums[i] + curMax);
        maxAns = Math.max(maxAns, curMax);
    }

    return maxAns;
};
```

- best time to buy and sell stocks 

```js
/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let maxP = 0;
    let l = 0;
    let r = 0;

    while(r < prices.length) {
        if(prices[l] < prices[r]) {
            maxP = Math.max(maxP, prices[r] - prices[l]);
        }
        else {
            l = r;
        }
        r++;
    }

    return maxP;
};
```

- Longest Substring Without Repeating Characters

```js
/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    let maxLength = 0;
    let i = 0;
    let j = 0;
    const set = new Set();

    if(!s.length) {
        return 0;
    }

    while(j < s.length) {
        if(set.has(s[j])) {
            set.delete(s[i]);
            i++;
        }
        else {
            set.add(s[j]);
            j++;
            maxLength = Math.max(maxLength, set.size);
        }
    }

    return maxLength;
};
```


- total sub arrays sum to k

```js
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var subarraySum = function(nums, k) {
    let count = 0;
    let p_sum = 0;
    const p_map = {
        0:1
    };

    for(let i=0;i<nums.length;i++) {
        p_sum += nums[i];

        if(p_map[p_sum - k] > 0) {
            count += p_map[p_sum - k];
        }
        if(!p_map[p_sum]) {
            p_map[p_sum] = 1
        }
        else {
            p_map[p_sum]++;
        }
    }

    return count;
};
```

- Longest Repeating Character Replacement

```js
/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var characterReplacement = function(s, k) {
    const windowHash = {};  
    let l = 0, r = 0;
    let maxLength = 0
    while(r < s.length) {
        const char = s.charAt(r);
        if(windowHash[char]) {
            windowHash[char]++;
        }
        else {
            windowHash[char] = 1;
        }

        // calculate the maxRepeatedChars
        let max = 0;
        Object.keys(windowHash).forEach(k => {
           max = Math.max(windowHash[k], max);
        });
        
        if((r - l + 1) - max <= k) {
            maxLength = Math.max(maxLength, (r - l + 1));
        }
        else {
            windowHash[s.charAt(l)]--;
            l++;
        }
        r++;
    }

    return maxLength;
};
```


- permutation in a string

```js
/**
 * @param {string} s1
 * @param {string} s2
 * @return {boolean}
 */
var checkInclusion = function(s1, s2) {
    if(s1.length > s2.length) return false;
    let l = 0, r = s1.length - 1;
    const hmS1 = new Array(26).fill(0);
    const hmS2 = new Array(26).fill(0);

    for(let s of s1) {
       hmS1[s.charCodeAt(0) - 97]++;
    }

    for(let s of s2.slice(0, s1.length)) {
        hmS2[s.charCodeAt(0) - 97]++;
    }

    while(r < s2.length) {
        // compare if both are equal
        let isEqual = true;
        for(let i=0;i<26;i++) {
            if(hmS1[i] != hmS2[i]) {
                isEqual = false;
            }
        }

        if(isEqual) return true;

        hmS2[s2.charCodeAt(l++) - 97]--;
        hmS2[s2.charCodeAt(++r) - 97]++;
    }

    return false;
};
```

- actual neetcode way of solving permutation in a string

```js
class Solution {
    /**
     * @param {string} s1
     * @param {string} s2
     * @return {boolean}
     */
    checkInclusion(s1, s2) {
        if(s1.length > s2.length) return false;

        const arr1 = new Array(26).fill(0);
        const arr2 = new Array(26).fill(0);

        for(let i=0;i<s1.length;i++) {
            const index1 = s1.charCodeAt(i) - 'a'.charCodeAt(0);
            const index2 = s2.charCodeAt(i) - 'a'.charCodeAt(0);

            arr1[index1]++;
            arr2[index2]++;
        }
        let matches = 0;
        for(let i=0;i<26;i++) {
            if(arr1[i] == arr2[i]) {
                matches++;
            }
        }

        let l = 0;
        for(let r=s1.length;r<s2.length;r++) {
             console.log(matches);
            if(matches == 26) return true;
            let idx = s2.charCodeAt(r) - 97;
            arr2[idx]++;
            if(arr1[idx] == arr2[idx]) {
                matches++;
            }
            else if(arr1[idx] + 1 == arr2[idx]) {
                matches--;
            }

            idx = s2.charCodeAt(l) - 97;
            arr2[idx]--;

            if(arr1[idx] == arr2[idx]) {
                matches++;
            }
            else if(arr1[idx] - 1 == arr2[idx]) {
                matches--;
            }

            l++;
        }

       
        return matches == 26;
    }    
}

```

- valid parenthesis

```js
/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    const stack = [];
    const map = {
        '(': ')',
        '{': '}',
        '[' : ']'
    };

    const revMap = {
        ')': '(',
        '}':  '{',
        ']': '['
    };

    for(let i of s) {
        if(map[i]) {
            stack.push(i);
        }
        else {
            const top = stack.pop();
            if(top !== revMap[i]) {
                return false;
            }
        }
    }

    return stack.length === 0;
};
```


- min stack time complexity

```js

var MinStack = function() {
   this.stack = [];

};

/** 
 * @param {number} val
 * @return {void}
 */
MinStack.prototype.push = function(val) {
    if(!this.stack.length) {
        this.stack.push([val, val]);
    }
    else {
        const lastIndex = this.stack.length - 1;
        this.stack.push([val, Math.min(val, this.stack[lastIndex][1])]);
    }
};

/**
 * @return {void}
 */
MinStack.prototype.pop = function() {
    this.stack.pop();
};

/**
 * @return {number}
 */
MinStack.prototype.top = function() {
    return this.stack[this.stack.length - 1][0];
};

/**
 * @return {number}
 */
MinStack.prototype.getMin = function() {
    return this.stack[this.stack.length - 1][1];
};

/** 
 * Your MinStack object will be instantiated and called as such:
 * var obj = new MinStack()
 * obj.push(val)
 * obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.getMin()
 */
```

- reverse polish notation

```js
/**
 * @param {string[]} tokens
 * @return {number}
 */
var evalRPN = function(tokens) {
    const validOperators = '+-*/';
    const stack = [];

    for(let i=0;i<tokens.length;i++) {
        if(validOperators.includes(tokens[i])) {
            const op1 = stack.pop();
            const op2 = stack.pop();
            let res;
            if(tokens[i] === '+') {
                res = op1 + op2;
            }
            else if(tokens[i] === '-') {
                res = op2 - op1;
            }
            else if(tokens[i] === '*') {
                res = op1 * op2;
            }
            else {
                res = op2 / op1;
                res = Math.trunc(res)
            }
            stack.push(res);
        }
        else {
            stack.push(Number(tokens[i]));
        }
    }

    return stack[0];
};  
```

- generate parenthesis

```js
/**
 * @param {number} n
 * @return {string[]}
 */
var generateParenthesis = function(n) {
    let output = [];
    let stack = [];
    

    const backtracking = (open, closed) => {
        if(open === closed && n === open) {
            output.push(stack.join(""));
            return;
        }

        if(open < n) {
            stack.push('(');
            backtracking(open + 1, closed);   
            stack.pop();
        }
        
        if(open > closed) {
            stack.push(')');
            backtracking(open, closed + 1);
            stack.pop();
        }
    }

    backtracking(0,0);

    return output;
};
```

- daily temperatures

```js
/**
 * @param {number[]} temperatures
 * @return {number[]}
 */
var dailyTemperatures = function(temperatures) {
    const stack = []; // [temp, index]
    const result = new Array(temperatures.length).fill(0);

    for (let i = 0; i < temperatures.length; i++) {
        const cT = temperatures[i];

        // First: resolve all smaller temps before current
        while (stack.length > 0 && cT > stack[stack.length - 1][0]) {
            const [, idx] = stack.pop();
            result[idx] = i - idx;
        }

        // Then push the current one
        stack.push([cT, i]);
    }

    return result;
};

```


- car fleet 

```js
/**
 * @param {number} target
 * @param {number[]} position
 * @param {number[]} speed
 * @return {number}
 */
var carFleet = function(target, position, speed) {
    // sort based on position
    const cData = position.map((pos, index) => {
        return [
            pos,
            speed[index]
        ];
    }).sort((a,b) => a[0] - b[0]);

    const stack = [];

    for(let i=cData.length-1;i>=0;i--) {
        const stackLastIndex = stack.length - 1;
        const currentTimeToReach = (target - cData[i][0]) / cData[i][1];
        if(stack.length > 0 && stack[stackLastIndex] >= currentTimeToReach) {
            continue;
        }

        stack.push(currentTimeToReach);
    }

    return stack.length; 
};
```


- binary search

```js
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function(nums, target) {
    let l = 0, r = nums.length - 1;

    while(l <= r) {
        const mid = Math.floor((l + r) / 2);
        if(nums[mid] > target) {
            r = mid - 1;
        }
        else if(nums[mid] < target) {
            l = mid + 1;
        }
        else {
            return mid;
        }
    }

    return -1;
};
```

- meeting rooms 

```js
/**
 * Definition of Interval:
 * class Interval {
 *   constructor(start, end) {
 *     this.start = start;
 *     this.end = end;
 *   }
 * }
 */

class Solution {
    /**
     * @param {Interval[]} intervals
     * @returns {boolean}
     */
    canAttendMeetings(intervals) {
        // sort based on the start time
        intervals.sort((a,b) => a.start - b.start);
        
        for(let i=1;i<intervals.length;i++) {
            // now check if next element start is coling with previous 
            // element start
            if(intervals[i].start < intervals[i-1].end) {
                return false;
            }
        }

        return true;
    }
}

```

- meeting rooms - II

```js
/**
 * Definition of Interval:
 * class Interval {
 *   constructor(start, end) {
 *     this.start = start;
 *     this.end = end;
 *   }
 * }
 */

class Solution {
    /**
     * @param {Interval[]} intervals
     * @returns {number}
     */
    minMeetingRooms(intervals) {
        let startTime = [];
        let endTime = [];

    
        for(let i=0;i<intervals.length;i++) {
            startTime.push(intervals[i].start);
            endTime.push(intervals[i].end);
        }

        startTime.sort((a,b) => a - b);
        endTime.sort((a,b) => a - b);

        
        let needMeetRoom = 0, i = 0, j = 0, n = intervals.length;
        let maxAns = 0;
        while(i < n && j < n) {
            if(startTime[i] < endTime[j]) {
                needMeetRoom++;
                maxAns = Math.max(maxAns, needMeetRoom);
                i++;
            }
            else {
                needMeetRoom--;
                j++;
            }
        } 

        return maxAns;
    }
}

```

- koko eating bananas

```js
/**
 * @param {number[]} piles
 * @param {number} h
 * @return {number}
 */
var minEatingSpeed = function(piles, h) {
    // min = 1
    // max = Math.max(piles)
    let low = 1 , high = 1;
    for(let i=0;i<piles.length;i++) {
        high = Math.max(high, piles[i]);
    }

    let mid;
    while(low <= high) {
        // now mid
        mid = Math.floor((low + high) / 2);

        // now check if eating these number of bananas can we complete all the piles
        let hoursLeft = h;
        for(let i=0;i<piles.length;i++) {
            hoursLeft -= Math.ceil(piles[i] / mid);
        }

        if(hoursLeft >= 0) {
            high = mid - 1;
        }
        else if(hoursLeft < 0) {
            low = mid + 1;
        }
        
    }

    return low;
};
```

- search a 2d matrix

```js
/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */
var searchMatrix = function(matrix, target) {
    // find the vertical row

    let top = 0, bottom = matrix.length - 1;
    let mid;
    while (top <= bottom) {
        mid = Math.floor((top + bottom) / 2);

        if(target < matrix[mid][0]) {
            bottom = mid - 1;
        }
        else if(target > matrix[mid][matrix[0].length - 1]) {
            top = mid + 1;
        }
        else {
            break;
        }
    }

    if(matrix[mid][0] > target || matrix[mid][matrix[0].length - 1] < target) {
        return false;
    }

    let l = 0, r = matrix[0].length - 1;
    while(l <= r) {
        let cmid = Math.floor((l + r) / 2);
        if(target < matrix[mid][cmid]) {
            r = cmid - 1;
        }
        else if(target > matrix[mid][cmid]) {
            l = cmid + 1;
        }
        else {
            return true;
        }
    }

    return false;
};
```

- find minimum in rotated sorted array

```js
    /**
 * @param {number[]} nums
 * @return {number}
 */
var findMin = function(nums) {  
    // O(log(n)) // roated sorted array 
    let l = 0, r = nums.length - 1, res = nums[0];


    while(l <= r) {
        const mid = Math.floor((l + r) / 2);
        if(nums[l] < nums[r]) {
            res = Math.min(nums[l], res);
            break;
        }

        res = Math.min(res, nums[mid]);
    
        if(nums[mid] >= nums[l]) {
            l = mid + 1;
        }
        else {
            r = mid - 1;
        }
        
    }

    return res;
};
```

- search in a rotated sorted array

```js
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function(nums, target) {
    let res = -1;
    let l = 0, r = nums.length - 1;

    while(l <= r) {
        const m = Math.floor((l + r) / 2 );

        if(nums[m] == target) return m;

        // left half is sorted
        if(nums[l] <= nums[m]) {
            if(target >= nums[l] && target < nums[m]) {
                r = m - 1;
            }
            else {
                l = m + 1;
            }
        }
        else {
            if (target > nums[m] && target <= nums[r]) {
                l = m + 1;
            } else {
                r = m - 1;
            }
        }
    }

    return -1;
};
```

- time based key value store

```js

var TimeMap = function() {
    this.object = {};
};

/** 
 * @param {string} key 
 * @param {string} value 
 * @param {number} timestamp
 * @return {void}
 */
TimeMap.prototype.set = function(key, value, timestamp) {
    if(!this.object[key]) {
        this.object[key] = [];
    }
    
    this.object[key].push([timestamp, value]);

    return null;
};

/** 
 * @param {string} key 
 * @param {number} timestamp
 * @return {string}
 */
TimeMap.prototype.get = function(key, timestamp) {
    // search the binary search 
    const data = this.object[key];
     if(!data) return "";
    let l = 0, r = data.length - 1;
 let res = "";
    while(l <= r) {
        let m = Math.floor((l + r) / 2);
       
        const [k, v] = data[m];
        
        if(k == timestamp) {
            return v;
        }

        if(k < timestamp) {
            res = v;
            l = m + 1;
        }
        else {
            r = m - 1;
        }
    }

    return res;
};

/** 
 * Your TimeMap object will be instantiated and called as such:
 * var obj = new TimeMap()
 * obj.set(key,value,timestamp)
 * var param_2 = obj.get(key,timestamp)
 */
```

- reversing the linked list

```js
/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var reverseList = function(head) {
    let prev = null;
    let cur = head;

    while(cur) {
        const next = cur.next;
        cur.next = prev;
        prev = cur;
        cur = next;
    }

    return prev;
};
```


- merge two sorted linked lists

```js
/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
var mergeTwoLists = function(list1, list2) {
    let head = new ListNode(0, null);
    let temp = head;
    let ptr1 = list1, ptr2 = list2;
    while(ptr1 && ptr2) {
        if(ptr1.val > ptr2.val) {
            temp.next = ptr2;
            ptr2 = ptr2.next;
        }
        else {
            temp.next = ptr1;
            ptr1 = ptr1.next;
        }

        temp = temp.next;
    }

    if(ptr1) {
        temp.next = ptr1;
    }
    else if(ptr2) {
        temp.next = ptr2;
    }

    return head.next;
};
```

- has cycle in linked list

```js
/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {boolean}
 */
var hasCycle = function(head) {
    let slow = head, fast = head;

    while(fast && fast.next) {
        slow = slow.next;
        fast = fast.next.next;
        if(slow == fast) {
            return true;
        }
    }

    return false;
};
```


- reorder linked list

```js
/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {void} Do not return anything, modify head in-place instead.
 */
var reorderList = function(head) {
    if(!head || !head.next) return;

    let slow = head;
    let fast = head;
    while(fast && fast.next) {
        slow = slow.next;
        fast = fast.next.next;
    }

    let ptr = slow.next;
    slow.next = null;
    // now reverse the linked list
    let newHead = null;
    while(ptr) {
        let next = ptr.next;
        ptr.next = newHead;
        newHead = ptr;
        ptr = next;
    }

    // merge the head with new reversed linked list 
    let dummyNode = new ListNode(0, null);
    temp = dummyNode;
    let takeFirst = true;
    while(head && newHead) {
        if(takeFirst) {
            temp.next = head;
            head = head.next;
        }
        else {
            temp.next = newHead;
            newHead = newHead.next;
        }

        temp = temp.next;
        takeFirst = !takeFirst;
    }   

    if(head) {
        temp.next = head;
    }

    if(newHead)
    {
        temp.next = newHead;
    }
};
```

- remove nth node from end

```js
/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */
var removeNthFromEnd = function(head, n) {
    let c = 0;
    let dummy = new ListNode(0, head);
    let temp = head;
    while(c != n) {
        temp = temp.next;
        c++;
    }

    let s = dummy;
    while(temp) {
        s = s.next;
        temp = temp.next;
    }

    s.next = s.next.next;
    
    
    return dummy.next;
};
```

- copy linked list with a random list

```js
/**
 * // Definition for a _Node.
 * function _Node(val, next, random) {
 *    this.val = val;
 *    this.next = next;
 *    this.random = random;
 * };
 */

/**
 * @param {_Node} head
 * @return {_Node}
 */
var copyRandomList = function(head) {
    const map = new Map();
    map.set(null, null);
    let cur = head;
    while(cur) {
        map.set(cur, new Node(cur.val))
        cur = cur.next;
    }

    cur = head;
    while(cur) {
        let copy = map.get(cur);
        copy.next = map.get(cur.next);
        copy.random = map.get(cur.random);
        cur = cur.next;
    }

    return map.get(head);
};
```

- Add Two Numbers

```js
/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) {
    let dummy = new ListNode();
    let carry = 0;
    let cur = dummy;
    while(l1 || l2 || carry) {
        let v1 = l1 ? l1.val : 0;
        let v2 = l2 ? l2.val : 0;

        let val = v1 + v2 + carry;
        carry = Math.floor(val / 10);
        val = val % 10;
        cur.next = new ListNode(val);

        cur = cur.next;
        l1 = l1 ? l1.next : null;
        l2 = l2 ? l2.next : null;
    }

    return dummy.next;
};
```


- find the duplicate numbers (floys algorithm using linked list cycle detection)

```js
/**
 * @param {number[]} nums
 * @return {number}
 */
var findDuplicate = function(nums) {
    // Floyds Tortoise and Hare Problem  
    let slow = 0, fast = 0;

    while(true) {
        slow = nums[slow]
        fast = nums[nums[fast]]
        if (slow == fast) {
            break;
        }
    }

    let slow2 = 0;
    while(true) {
        slow = nums[slow]
        slow2 = nums[slow2]
        if(slow === slow2) {
            return slow;
        }
    }
};
```

-- lru cache

```js
class Node {
    constructor(key, val) {
        this.key = key;
        this.val = val;
        this.next = null;
        this.prev = null;
    }
}

/**
 * @param {number} capacity
 */
var LRUCache = function(capacity) {
    this.capacity = capacity;
    this.cache = new Map();
    this.start = new Node(0,0);
    this.end = new Node(0,0);
    this.start.next = this.end;
    this.end.prev = this.start;
};

LRUCache.prototype._remove = function(node) {
    node.prev.next = node.next;
    node.next.prev = node.prev;
};

LRUCache.prototype._insert = function(node) {
    node.prev = this.end.prev;
    node.next = this.end;
    this.end.prev.next = node;
    this.end.prev = node;
};


/** 
 * @param {number} key
 * @return {number}
 */
LRUCache.prototype.get = function(key) {
    // check if the key is present in map
    const node = this.cache.get(key)
    if(!node) {
        return -1;
    }

    // delete the key 
    this._remove(node);
    // insert the key
    this._insert(node);
    return node.val;
    
};

/** 
 * @param {number} key 
 * @param {number} value
 * @return {void}
 */
LRUCache.prototype.put = function(key, value) {
    if(this.cache.has(key)) {
        const node = this.cache.get(key);
        node.val = value;
        this._remove(node);
        this._insert(node);
        return;
    }
    let node = new Node(key, value);
    this.cache.set(key, node);
    this._insert(node);
    if(this.cache.size > this.capacity) {
        let lru = this.start.next;
        this._remove(lru);
        this.cache.delete(lru.key);
    }
};

/** 
 * Your LRUCache object will be instantiated and called as such:
 * var obj = new LRUCache(capacity)
 * var param_1 = obj.get(key)
 * obj.put(key,value)
 */
```

- Invert Binary Tree

```js
/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     constructor(val = 0, left = null, right = null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    /**
     * @param {TreeNode} root
     * @return {TreeNode}
     */
    invertTree(root) {
        if(!root) return null;
        
        let temp = root.left;
        root.left = root.right;
        root.right = temp;

        this.invertTree(root.left);
        this.invertTree(root.right);


        return root;
    }
}
```

- max depth of a tree

```js
class Solution {
    maxDepth(root) {
        if (!root) return 0;
        
        const leftDepth = this.maxDepth(root.left);
        const rightDepth = this.maxDepth(root.right);
        
        return 1 + Math.max(leftDepth, rightDepth);
    }
}

```

- same above solution but level order traversal 

```js
class Solution {
    maxDepth(root) {
        if(!root) return 0;
        let queue = [root];
        let level = 0;
        while(queue.length) {
            let len = queue.length;
            for(let i=0;i<len;i++) {
                const cur = queue.shift();
                if(cur.left) {
                    queue.push(cur.left);
                }
                if(cur.right) {
                    queur.push(cur.right);
                }
            }

            level += 1;
        }
    
        return level;
    }
}
```


- diameter of binary tree

```js
/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     constructor(val = 0, left = null, right = null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    /**
     * @param {TreeNode} root
     * @return {number}
     */
    diameterOfBinaryTree(root) {
        if(!root) return 0;

        let diameter = 0;

        const depth = (ptr) => {
            if(!ptr) return 0;

            let lDp = depth(ptr.left);
            let rDp = depth(ptr.right);

            diameter = Math.max(lDp + rDp , diameter);

            return 1 + Math.max(lDp, rDp);
        }

        depth(root, 0);
        return diameter;
    }
}

```


- is binary tree balanced or not

```js
/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     constructor(val = 0, left = null, right = null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    

    /**
     * @param {TreeNode} root
     * @return {boolean}
     */
    isBalanced(root) {
        let glob = true;

        const depth = (ptr) => {
            if(!ptr) return 0;
            let left = depth(ptr.left);
            let right = depth(ptr.right);

            if(Math.abs(left - right) > 1) {
                glob = false;
            }

            return 1 + Math.max(left, right);
        }

        depth(root);
       
        return glob;
    }
}

```

- is same tree

```js
/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     constructor(val = 0, left = null, right = null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    /**
     * @param {TreeNode} p
     * @param {TreeNode} q
     * @return {boolean}
     */
    isSameTree(p, q) {
        if(!p && !q) return true;
        if(!p || !q || p.val != q.val) return false;

        let leftEqual = this.isSameTree(p.left, q.left);
        let rightEqual = this.isSameTree(p.right, q.right);
        return leftEqual && rightEqual;
    }
}

```

- lowest common ancestor

```js
/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     constructor(val = 0, left = null, right = null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    /**
     * @param {TreeNode} root
     * @param {TreeNode} p
     * @param {TreeNode} q
     * @return {TreeNode}
     */
    lowestCommonAncestor(root, p, q) {
        let cur = root;

        while(cur) {
            if(p.val < cur.val && q.val < cur.val) {
                cur = cur.left;
            }
            else if(p.val > cur.val && q.val > cur.val) {
                cur = cur.right;
            }
            else {
                return cur;
            }
        }
    }
}

```

- sub tree of another tree

```js
/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     constructor(val = 0, left = null, right = null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    constructor() {
        this.res = [];
    }

    isSameTree(p, q) {
        if(!p && !q) return true;
        if(!p || !q || p.val != q.val) return false;
        return (this.isSameTree(p.left, q.left) && this.isSameTree(p.right, q.right));
    }

    dfs(cur, val) {
        if(!cur) {
            return null;
        }

        if(cur.val == val) {
            this.res.push(cur);
        }

        this.dfs(cur.left, val);
        this.dfs(cur.right, val);
    
    }

    /**
     * @param {TreeNode} root
     * @param {TreeNode} subRoot
     * @return {boolean}
     */
    isSubtree(root, subRoot) {
        // find the subroot node first in root
        if(!root && !subRoot) {
            return true;
        }
        if(root && !subRoot) {
            return true;
        }
        if(!root && subRoot) {
            return false;
        }

        this.res = [];

        this.dfs(root, subRoot.val);
        if(this.res.length) {
            let isSameTree = false;
            for(let i=0;i<this.res.length;i++) {
                if(this.isSameTree(this.res[i], subRoot)) {
                    isSameTree = true;
                }
            }

            return isSameTree;
        }
        else {
            return false;
        }
    }
}

```

- binary tree level order traversal

```js
/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     constructor(val = 0, left = null, right = null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    /**
     * @param {TreeNode} root
     * @return {number[][]}
     */
    levelOrder(root) {
        if(!root) return [];
        const res = [];
        let q = [root];
        while (q.length) {
            const l = q.length;
            const lres = [];
            for(let i=0;i<l;i++) {
                let node = q.shift();
                lres.push(node.val);
                node.left ? q.push(node.left) : null;
                node.right ? q.push(node.right): null;
            }
            res.push(lres);
        }

        return res;
    }
}
```


- good nodes in binary tree

```js
/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     constructor(val = 0, left = null, right = null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    /**
     * @param {TreeNode} root
     * @return {number}
     */
    goodNodes(root) {
        if(!root) return 0;
        let count = 0;
        const dfs = (cur, max) => {
            const node = cur;
            if(node.val >= max) {
                count++;
                max = node.val;
            }           

            cur.left ? dfs(cur.left, max) : null;
            cur.right ? dfs(cur.right, max) : null;
        }

        dfs(root, -Infinity);

        return count;
    }
}

```

- binary tree right side view

```js
/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     constructor(val = 0, left = null, right = null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    /**
     * @param {TreeNode} root
     * @return {number[]}
     */
    rightSideView(root) {
        // in order traversal + last most element
        if(!root) return [];
        let q = [root];
        let res = [];
        while(q.length) {
            let len = q.length;
            for(let i=0;i<len;i++) {
                let n = q.shift();
                if(i == len - 1) {
                    res.push(n.val);
                }
                n.left ? q.push(n.left) : null;
                n.right ? q.push(n.right) : null;
            }
        }

        return res;
    }
}

```

- is a valid binary search tree


```js
/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     constructor(val = 0, left = null, right = null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    /**
     * @param {TreeNode} root
     * @return {boolean}
     */
    isValidBST(root) {
        // in order adding new element value should be grater >=
        if(!root) return true;
        const order = [];
        let isValid = true;
        const dfs = (cur) => {
            if(!cur || !isValid) return;
            // check validity
            cur.left && dfs(cur.left);
            if(order.length == 0 || order[order.length - 1] < cur.val) {
                order.push(cur.val);
            }
            else {
                isValid = false;
                return;
            }
            
            cur.right && dfs(cur.right);
        };

        dfs(root);
        return isValid;
    }
}

```



### Alternative approach for valid bst maintaining a left most valid , right most valid boundaries

A node in a BST isn’t checked only against its parent, but against the **entire chain of ancestors**.  
Each recursive call carries a value-range `(left, right)` that the current node must fit inside.

- When moving **left**, the `right` bound becomes `node.val`.
- When moving **right**, the `left` bound becomes `node.val`.

If any node breaks its allowed range, the whole tree fails the BST test.

---

##### Time Complexity

`O(n)` — every node is visited exactly once,  
and the bound checks (`val > left` and `val < right`) are constant-time.

---

##### Space Complexity

`O(h)` — where `h` is the height of the tree.

This comes from the recursion stack:

- **Balanced tree:** `h = log n` → space is `O(log n)`
- **Skewed tree (like a linked list):** `h = n` → space is `O(n)`

No extra data structures are used beyond the recursion stack.

---

```js
class Solution {
    isValidBST(root) {
        const helper = (node, left = -Infinity, right = Infinity) => {
            if (!node) return true;
            if (!(node.val < right && node.val > left)) return false;

            return helper(node.left, left, node.val) &&
                   helper(node.right, node.val, right);
        };

        return helper(root);
    }
}
```


- Kth Smallest Element In a BST

- iterative dfs and maintain total nodes visited and for k print the value

```js
/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     constructor(val = 0, left = null, right = null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    /**
     * @param {TreeNode} root
     * @param {number} k
     * @return {number}
     */
    kthSmallest(root, k) {
        let n = 0;
        let cur = root;
        let stack = [];
        while(cur || stack) {
            while(cur) {
                stack.push(cur);
                cur = cur.left;
            }
            cur = stack.pop();
            n += 1;
            if(n == k) {
                return cur.val;
            }
            cur = cur.right;
        }
    }
}

```

- Construct Binary Tree From Preorder & Inorder

```js
/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     constructor(val = 0, left = null, right = null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    constructor() {
        this.indexes = {};   // value -> index in inorder
        this.preIndex = 0;   // pointer in preorder
    }

    dfs(preorder, left, right) {
        // left & right are bounds in inorder array
        if (left > right) return null;

        // pick current root from preorder
        const rootVal = preorder[this.preIndex++];
        const root = new TreeNode(rootVal);

        // find root position in inorder in O(1)
        const mid = this.indexes[rootVal];

        // build left and right subtrees
        root.left = this.dfs(preorder, left, mid - 1);
        root.right = this.dfs(preorder, mid + 1, right);

        return root;
    }

    /**
     * @param {number[]} preorder
     * @param {number[]} inorder
     * @return {TreeNode}
     */
    buildTree(preorder, inorder) {
        this.preIndex = 0;
        this.indexes = {};

        // map each value to its index in inorder
        inorder.forEach((v, index) => {
            this.indexes[v] = index;
        });

        return this.dfs(preorder, 0, inorder.length - 1);
    }
}

```

### Intervals Problems

- Insert Interval

```js
class Solution {
    /**
     * @param {number[][]} intervals
     * @param {number[]} newInterval
     * @return {number[][]}
     */
    insert(intervals, n) {
        let newInterval = n;
        const res = [];

        for(let i=0;i<intervals.length;i++) {
            // not overlapping & matchig
            if(newInterval[1] < intervals[i][0]) {
                res.push(newInterval);
                return [...res, ...intervals.slice(i)];
            }
            // not overlapping and not in the range
            else if(newInterval[0] > intervals[i][1]) {
                res.push(intervals[i]);
            }
            else {
                newInterval = [
                    Math.min(newInterval[0], intervals[i][0]),
                    Math.max(newInterval[1], intervals[i][1])
                ]
            }
        }
        res.push(newInterval);

        return res;
    }
}

```

- Merge Intervals

```js

class Solution {
    /**
     * @param {number[][]} intervals
     * @return {number[][]}
     */
    merge(intervals) {
        const res = [];
        let sortedInt = [];
        if(Array.isArray(intervals)) {
            sortedInt = intervals.sort((a, b) => {
            return a[0] - b[0];
        });
        }
        for(let i=0;i<sortedInt.length;i++) {
            if(!res.length) {
                res.push(intervals[i]);
                continue;
            }

            // get the last overlapping
            const lastItem = res.length - 1;
            const endItem = res[lastItem][1];

            if(intervals[i][0] > endItem) {
                res.push(intervals[i]);
            }
            else {
                res[lastItem][1] = Math.max(endItem, intervals[i][1]);
            }
        }

        return res;
    }
}
```

- Non Overlapping Intervals (My Solution)
 
```js
class Solution {
    /**
     * @param {number[][]} intervals
     * @return {number}
     */
    eraseOverlapIntervals(intervals) {
        let sInt = intervals.sort((a, b) => a[0] - b[0]);
        let res = [sInt[0]];

        for(let i=1;i<sInt.length;i++) {
            const li = res.length - 1;
            const lastItem = res[li][1];

            if(lastItem <= sInt[i][0]) {
                res.push(sInt[i]);
            }
            else {
                res[li][1] = Math.min(res[li][1], sInt[i][1]);
            }
        }
        return sInt.length - res.length;
    }
}

```

- solution as per neetcode

```js
class Solution {
    /**
     * @param {number[][]} intervals
     * @return {number}
     */
    eraseOverlapIntervals(intervals) {
        let sInt = intervals.sort((a, b) => a[1] - b[1]);
        let prevEnd = -Infinity;
        let res = 0;
        for(let i=0;i<sInt.length;i++) {
            if(sInt[i][0] >= prevEnd) {
                res++;
                prevEnd = sInt[i][1];
            }
        }
        return sInt.length - res;
    }
}
```

### Bit Manipulation

- single number


```js
class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    singleNumber(nums) {
        let ans = nums[0];
        for(let i=1;i<nums.length;i++) {
            ans ^= nums[i];
        }

        return ans;
    }
}

```

- Number of 1 Bit

```js
class Solution {
    /**
     * @param {number} n - a positive integer
     * @return {number}
     */
    hammingWeight(n) {
        let count = 0;
        
        while(n) {
            count += n & 1;
            n >>= 1;
        }
       
        return count;
    }
}

```

- efficient answer for num of 1 bits

> Whenever you do n &= (n - 1), you slice off the rightmost 1-bit from n.

```js
class Solution {
    /**
     * @param {number} n - a positive integer
     * @return {number}
     */
    hammingWeight(n) {
        let count = 0;
        
        while(n) {
            n &= (n - 1);
            count++;
        }
       
        return count;
    }
}

```

- Counting Bits

> this involves dynamic programming + bit manipulation.

```js
class Solution {
    /**
     * @param {number} n
     * @return {number[]}
     */
    countBits(n) {
        let dp = new Array(n+1).fill(0);
        let offset = 1;

        for(let i=1;i<=n;i++) {
            if(offset * 2 == i) {
                offset = i;
            }
            dp[i] = 1 + dp[i - offset];
        }
        return dp;
    }
}

```

- reverse bits

```js
class Solution {
    /**
     * @param {number} n - a positive integer
     * @return {number} - a positive integer
     */
    reverseBits(n) {
        let rep = 0;
        let ans = 0;
        while(rep < 32) {
            if(n % 2) {
                 ans += Math.pow(2, 31 - rep);
            }
            n >>= 1;
            rep++;
        }
        

        return ans;
    }
}

```

- same reverse bits but neetcode optimised way by shifting the bit wise operators 

```js
class Solution {
    /**
     * @param {number} n - a positive integer
     * @return {number} - a positive integer
     */
    reverseBits(n) {
        let res = 0;
        for(let i=0;i<32;i++) {
            let l = (n >>> i) & 1;
            res = res | (l << (31 - i))
        }

        return res >>> 0;
    }
}
```


- missing number

```js
class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    missingNumber(nums) {
          let res;
          for(let i=0;i<=nums.length;i++) {
            res ^= i ^ nums[i];
          }      

        return res;
    }
}

```

### Backtracking

- subsets

```js

class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    subsets(nums) {
        const output = [];
        const res = [];
        const dfs = (n = 0) => {
            // base case
            if(nums.length == n) {
                output.push([...res]);
                return;
            }
            res.push(nums[n]);
            dfs(n+1);
            res.pop();
            dfs(n + 1);
        }

        dfs();

        return output;
    }
}

```

- combination sum (my version)
 
```js
class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @returns {number[][]}
     */
    combinationSum(nums, target) {
        const output = [];
        nums.sort((a,b) => a - b);
        const res = [];
        const dfs = (curSum = 0, index = 0) => {
            if(curSum == target) {
                output.push([...res]);
                return;
            }
            
            if(curSum > target) {
                return;
            }
            for(let i=index;i<nums.length;i++) {
                res.push(nums[i]);
                const cur = res.reduce((acc, cur) => acc + cur, 0);
                dfs(cur, i);
                res.pop();
            }
        }   
        dfs();
        return output;
    }
}

```

- counting sum ii

```js
class Solution {
    /**
     * @param {number[]} candidates
     * @param {number} target
     * @return {number[][]}
     */
    combinationSum2(candidates, target) {
        const output = [];
        candidates.sort((a,b) => a - b);
        const res = [];
        const dfs = (sum = 0, index = 0) => {
            if(sum == target) {
                output.push([...res]);
                return;
            }
            if(sum > target) {
                return;
            }

            for(let i=index;i<candidates.length;i++) {
                if(i > index && candidates[i] == candidates[i-1]) {
                    continue;
                }
                res.push(candidates[i]);
                const sum = res.reduce((acc, s) => acc + s, 0);
                dfs(sum, i + 1);
                res.pop(); 
            }
        }   


        dfs();
        return output;
    }
}
```

- permutations

```js
class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    permute(nums) {
        const res = [];
        const dfs = (out = [], set = new Set()) => {
            if(set.size === nums.length) {
                res.push([...out]);
                return;
            }

            for(let i=0;i<nums.length;i++) {
                if(set.has(nums[i])){
                    continue;
                }
                out.push(nums[i]);
                set.add(nums[i]);
                dfs(out,set);
                set.delete(nums[i]);
                out.pop();
            }
        }

        dfs();

        return res;
    }
}

```

- subsets II

```js
class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    subsetsWithDup(nums) {
        const output = [];
    
        nums.sort((a,b) => a - b);
        const dfs = (n = 0, res = []) => {
            if(n === nums.length) {
                output.push([...res]);
                return;
            }
            res.push(nums[n]);
            dfs(n+1, res);
          
            while(n + 1 < nums.length && nums[n] == nums[n+1]) {
                n++;
            }
            res.pop();
            dfs(n+1, res);
        };
        dfs();
        return output;
    }
}

```


- generate parenthesis


```js
class Solution {
    /**
     * @param {number} n
     * @return {string[]}
     */
    generateParenthesis(n) {
        const output = [];
        const stk = [];
        const dfs = (open = 0, close = 0) => {
            if(open == n && close == n) {
                output.push(stk.join(''));
                return;
            }

            if(open < n) {
                stk.push('(');
                dfs(open + 1, close);
                stk.pop();
            }
            
            if(close < open) {
                stk.push(')');
                dfs(open, close + 1);
                stk.pop();
            }
        }
        dfs();
        return output;
    }
}

```

- word search

```js
class Solution {
    /**
     * @param {character[][]} board
     * @param {string} word
     * @return {boolean}
     */
    exist(board, word) {
        if (!board || board.length === 0 || !word) return false;

        const M = board.length;
        const N = board[0].length;
        const path = new Set();

        const dfs = (x, y, i) => {
            const key = `${x},${y}`;
            if(i === word.length) {
                return true;
            }

            if(x < 0 || y < 0 
                || x >= M 
                || y >= N 
                || path.has(key) 
                || board[x][y] !== word[i]
            ) {
                return false;
            }

            path.add(key);
            const res = dfs(x + 1, y, i + 1) ||
                        dfs(x - 1, y, i+1) ||
                        dfs(x, y+1,i+1) || dfs(x, y - 1, i+1)
            path.delete(key);
            return res;
        }
        
        
       
        for(let i=0;i<M;i++) {
            for(let j=0;j<N;j++) {
                if(board[i][j] === word[0] && dfs(i, j, 0)) {
                    return true;
                }
            }
        }

        return false;
    }
}

```


- palindrome partiotining

```js
class Solution {
    /**
     * @param {string} s
     * @return {string[][]}
     */
    partition(s) {
        // palindrome string
        const res = [];
        const part = [];

        const dfs = (i = 0) => {
            if(i >= s.length) {
                res.push([...part]);
                return;
            }

            for(let j=i;j<s.length;j++) {
                if(this.isPali(s, i, j)) {
                    part.push(s.slice(i, j+1));
                    dfs(j+1)
                    part.pop();
                }
            }
        }

        dfs();
        return res;
    }

    isPali(s, l, r)
    {
        while(l < r) {
            if(s[l] != s[r]){
                return false;
            }
            l++;
            r--;
        }
        return true;
    }
 }

```

- letter combinations of a phone number

```js
class Solution {
    /**
     * @param {string} digits
     * @return {string[]}
     */
    letterCombinations(digits) {
        const digitToChar = {
            2: 'abc',
            3: 'def',
            4: 'ghi',
            5: 'jkl',
            6: 'mno',
            7: 'qprs',
            8: 'tuv',
            9: 'wxyz',
        };

        const res = [];

        const backtrack = (i, cstr) => {
            if(cstr.length == digits.length) {
                res.push(cstr);
                return;
            }
            const str = digitToChar[digits[i]];
            for(let j = 0;j<str.length;j++) {
                backtrack(i+1, cstr + str[j]);
            } 
        }
        if(digits) {
            backtrack(0, "");
        }
        return res;
    }
}

```

- successfulPairs (binary search)

```js
/**
 * @param {number[]} spells
 * @param {number[]} potions
 * @param {number} success
 * @return {number[]}
 */
var successfulPairs = function(spells, potions, success) {
    const output = [];
    potions.sort((a, b) => a - b); // sort ascending

    const firstIndexAtLeast = (search) => {
        let l = 0, r = potions.length - 1;
        let res = potions.length; // default: not found

        while (l <= r) {
            const m = Math.floor((l + r) / 2);

            if (potions[m] >= search) {
                res = m;      // candidate index
                r = m - 1;    // try to find an even smaller index
            } else {
                l = m + 1;
            }
        }

        // if res == potions.length, there is no potion >= search
        return res === potions.length ? 0 : potions.length - res;
    };

    for (let spell of spells) {
        // spell * potion >= success  => potion >= success / spell
        const search = Math.ceil(success / spell);
        const count = firstIndexAtLeast(search);
        output.push(count);
    }

    return output;
};

```

- matcsticks to square

https://leetcode.com/problems/matchsticks-to-square/ 

```js
/**
 * @param {number[]} matchsticks
 * @return {boolean}
 */
var makesquare = function(matchsticks) {
    const sum = matchsticks.reduce((a, s) => a + s, 0);
    const length = Math.floor(sum / 4);
    if(sum / 4 !== length) {
        return false;
    }
    const sides = new Array(4).fill(0);
    matchsticks.sort((a, b) => b - a);
    function backtracking(i) {
        if(i === matchsticks.length) { 
            return true;
        }

        for(let j=0;j<4;j++) {
            if(sides[j] + matchsticks[i] <= length) {
                sides[j] += matchsticks[i];
                if(backtracking(i + 1)) {
                    return true;
                }
                sides[j] -= matchsticks[i];
            }
        }

        return false;
    }
    
    return backtracking(0);
};
```

- number of islands 

```js
class Solution {
    /**
     * @param {character[][]} grid
     * @return {number}
     */
    numIslands(grid) {
        const rows = grid.length;
        const cols = grid[0].length;
        const visited = Array.from({length: rows}, () => {
            return Array(cols).fill(false);
        });
        const directions = [[0,1],[0,-1],[1,0],[-1,0]]
        let res = 0;
        function bfs(i, j) {
            const q = [[i,j]];
            visited[i][j] = true;
            while(q.length) {
                const [r, c] = q.shift();
                for(let dir of directions) {
                    const nx = r + dir[0];
                    const ny = c + dir[1];
                    if(nx >= 0 && nx < rows && ny >= 0 && ny < cols && !visited[nx][ny] && grid[nx][ny] === '1'){
                            visited[nx][ny] = true;
                            q.push([nx,ny]);
                    }
                }
            }
        }

        for(let i=0;i<rows;i++) {
            for(let j=0;j<cols;j++) {
                if(!visited[i][j] && grid[i][j] === '1') {
                    bfs(i, j);
                    res++;
                }
            }
        }

        return res;
    }
}

```

- max area of island

```js
class Solution {
    /**
     * @param {number[][]} grid
     * @return {number}
     */
    maxAreaOfIsland(grid) {
        const rows = grid.length;
        const cols = grid[0].length;
        const vis = Array.from({length: rows}, () => Array(cols).fill(false));
        let max = 0;
        const dir = [[0,1],[0,-1],[-1,0],[1,0]];
        const bfs = (i, j) => {
            const q = [[i,j]];
            let count = 1;
            if(!vis[i][j]) {
                vis[i][j] = true;
            }

            while(q.length) {
                const [qR,qC] = q.shift();
                for(let d of dir) {
                    const [nX, nY] = [qR + d[0], qC + d[1]];
                    if(
                        nX >= 0 && nX < rows 
                        && nY >= 0 && nY < cols
                        && !vis[nX][nY] 
                        && grid[nX][nY] === 1
                    ) {
                        count++;
                        vis[nX][nY] = true;
                        q.push([nX, nY]);
                    }
                }
            }

            return count;
        }

        for(let i=0;i<rows;i++) {
            for(let j=0;j<cols;j++) {
                if(!vis[i][j] && grid[i][j] === 1) {
                    max = Math.max(max, bfs(i,j));
                }
            }
        }

        return max;
    }
}

```

- clone graph

```js

/**
 * // Definition for a Node.
 * class Node {
 *     constructor(val = 0, neighbors = []) {
 *       this.val = val;
 *       this.neighbors = neighbors;
 *     }
 * }
 */

class Solution {
    /**
     * @param {Node} node
     * @return {Node}
     */
    cloneGraph(node) {
        if(!node) return null;
        
        const dopal = new Map();
        let clone = new Node(node.val);
        const q = [node];
        dopal.set(node, clone);
        while(q.length) {
            const item = q.shift();
            
            for(let nei of item.neighbors) {
                if(!dopal.has(nei)) {
                    q.push(nei);
                    dopal.set(nei, new Node(nei.val));
                }

                dopal.get(item).neighbors.push(dopal.get(nei));
            }
        }

        return clone;
    }
}

```

- clone graph with dfs

```js
/**
 * // Definition for a Node.
 * class Node {
 *     constructor(val = 0, neighbors = []) {
 *       this.val = val;
 *       this.neighbors = neighbors;
 *     }
 * }
 */

class Solution {
    /**
     * @param {Node} node
     * @return {Node}
     */
    cloneGraph(node) {
        if(!node) return null;
        const map = new Map();
        const dfs = (node) => {
            if(map.get(node)) {
                return map.get(node);
            }

            const clone = new Node(node.val);
            map.set(node, clone);
            for(let n of node.neighbors) {
                clone.neighbors.push(dfs(n));
            }

            return clone;
        }

        return dfs(node);
    }
}

```

- walls & gates graph problem

```js
class Solution {
    /**
     * @param {number[][]} grid
     */
    islandsAndTreasure(grid) {
        const ROWS = grid.length;
        const COLS = grid[0].length;
        const vis = new Set();
        const q = [];
        
        for(let i=0;i<ROWS;i++) {
            for(let j=0;j<COLS;j++) {
                if(grid[i][j] === 0) {
                    q.push([i, j]);
                    vis.add(`${i}-${j}`)
                }
            }
        }
        
        const add = (i,j) => {
            if(i < 0 || i === ROWS || j < 0 || j === COLS || vis.has(`${i}-${j}`) || grid[i][j] === -1) {
                return;
            }
            vis.add(`${i}-${j}`);
            q.push([i,j]);
        } 

        let dist = 0;
        while(q.length) {
            let l = q.length;
            for (let i=0;i<l;i++) {
                const [r, c] = q.shift();
                grid[r][c] = dist;
                add(r + 1, c);
                add(r - 1, c);
                add(r , c + 1);
                add(r , c - 1);  
            }
            dist += 1
        }
    }
}

```

- rotten oranges

```js
class Solution {
    /**
     * @param {number[][]} grid
     * @return {number}
     */
    orangesRotting(grid) {
        const ROWS = grid.length;
        const COLS = grid[0].length;
        const vis = new Set();
        const q = [];
        for(let i=0;i<ROWS;i++) {
            for(let j=0;j<COLS;j++) {
                if(grid[i][j] === 2) {
                    q.push([i,j]);
                    vis.add(`${i}-${j}`);
                }
            }
        }

        const add = (r,c) => {
            if(r < 0 || r === ROWS || c < 0 || c === COLS || vis.has(`${r}-${c}`) || grid[r][c] === 0) {
                return;
            }
            vis.add(`${r}-${c}`);
            q.push([r,c]);
        }

        let dist = 2;
        let maxDist = 2;
        while(q.length) {
            const len = q.length;
            for(let i=0;i< len;i++) {
                const [r, c] = q.shift();
                grid[r][c] = dist;
                maxDist = Math.max(maxDist, dist);
                add(r + 1, c);
                add(r - 1, c);
                add(r, c + 1);
                add(r, c - 1);
            }
            dist++;
        }

        for(let i=0;i<ROWS;i++) {
            for(let j=0;j<COLS;j++) {
                if(grid[i][j] === 1) return -1;
            }
        }

        return maxDist - 2;
    }
}

```

### Heaps

- K Closest Points to Origin

```py
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        data = []
        for x in points:
            x1, y1 = x
            dist = ((x1) ** 2 + (y1) ** 2) ** 1/2
            data.append((-dist, x))
        heapq.heapify(data)
        while len(data) != k:
            heapq.heappop(data)
        t_data = list(map(lambda x: x[1] ,data))
        return t_data
```

- Kth Largest Element in a Stream

```py

import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        self.k = k
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]
        

```

Last Stone Weight

```py
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        data = [-d for d in stones]
        heapq.heapify(data)
        while len(data) >= 2:
            big = -heapq.heappop(data)
            next_big = -heapq.heappop(data)
            w = abs(big - next_big)
            if w != 0:
                heapq.heappush(data, -w)
        if len(data):
            d = heapq.heappop(data)
            return -d
        else:
            return 0
       
```

Pacific Atlantic Water Flow 

```py
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac , atl = set(), set()

        def dfs(r, c, visit, prevHeight):
            if (r, c) in visit or r < 0 or c < 0 or r == ROWS or c == COLS or heights[r][c] < prevHeight:
                return 
            visit.add((r,c))
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])
        
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])
        
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r,c])
        return res


```

Surrounded Regions

```py
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c] != 'O':
                return
            board[r][c] = 'T'
            dfs(r, c + 1)
            dfs(r, c - 1)
            dfs(r + 1, c)
            dfs(r - 1, c)
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O' and (r in [0, ROWS - 1] or c in [0 , COLS - 1]):
                    dfs(r, c)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                
                if board[r][c] == 'T':
                    board[r][c] = 'O'
        
```

Course Schedule

```py
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = { i: [] for i in range(numCourses) }
        
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        vis = set()

        def dfs(crs):
            if crs in vis:
                return False
            if preMap[crs] == []:
                return True
            
            vis.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): 
                    return False
            vis.remove(crs)
            preMap[crs] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True

```

Course Schedule - II

```py
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = { c: [] for c in range(numCourses) }
        for cse, pre in prerequisites:
            prereq[cse].append(pre)
        vis, cyc = set(), set()
        output = []
        def dfs(crs):
            if crs in cyc:
                return False
            if crs in vis:
                return True
            
            cyc.add(crs)
            
            for pre in prereq[crs]:
                if not dfs(pre):
                    return False
            
            cyc.remove(crs)
            vis.add(crs)
            output.append(crs)
            return True


        for c in range(numCourses):
            if not dfs(c):
                return []
        
        return output
```