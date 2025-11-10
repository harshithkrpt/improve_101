
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
        console.log(str);
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

- multipy of numbers except seld


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