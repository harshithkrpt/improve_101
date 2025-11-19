
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

- daily temperatures

```js
/**
 * @param {number[]} temperatures
 * @return {number[]}
 */
var dailyTemperatures = function(temperatures) {
    const stack = [];
    const result = new Array(temperatures.length).fill(0);
    for(let i=0;i<temperatures.length;i++) {
        const top = stack.length - 1;
        if(stack.length === 0 || stack[top][0] > temperatures[i]) {
             stack.push([temperatures[i], i]);
        }
    
        const cT = temperatures[i];
        while(stack.length > 0 && cT > stack[stack.length-1][0]) {
            const popped = stack.pop();
            result[popped[1]] = i - popped[1];
        }

        stack.push([temperatures[i], i]);
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