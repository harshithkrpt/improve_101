class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr = [0] * 26

        for ch in s:
            arr[ord(ch) - ord('a')] += 1
        
        for ch in t:
            arr[ord(ch) - ord('a')] -= 1
        
        for n in arr:
            if n is not 0:
                return False
        
        return True