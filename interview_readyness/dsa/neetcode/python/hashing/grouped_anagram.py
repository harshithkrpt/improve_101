from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = []
        # Generate the Keys of all the list items 
        keys = {}
        for string in strs:
            currentKey = [0] * 26
            for ch in string:
                currentKey[ord(ch) - ord("a")] += 1
            currentKey = "-".join([str(n) for n in currentKey])
            if currentKey in keys:
                keys[currentKey].append(string)
            else:
                keys[currentKey] = [string]
        for k in keys:
            grouped.append(keys[k])
        
        return grouped
        
    