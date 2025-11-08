
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