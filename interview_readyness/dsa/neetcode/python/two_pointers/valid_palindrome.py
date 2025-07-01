# Valid Palindrome
# Solved 
# Given a string s, return true if it is a palindrome, otherwise return false.

# A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

# Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

# Example 1:

# Input: s = "Was it a car or a cat I saw?"

# Output: true
# Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.

# Example 2:

# Input: s = "tab a cat"

# Output: false
# Explanation: "tabacat" is not a palindrome.


class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid_string = ""
        for ch in s:
            if((ord(ch) >= ord('a') and ord(ch) <= ord('z')) or (ord(ch) >= ord('A') and ord(ch) <= ord('Z'))):
                valid_string = valid_string + ch
            if ord(ch) >= ord('0') and ord(ch) <= ord('9'):
                valid_string = valid_string + ch
        
        valid_string = valid_string.lower()

        l = 0
        r = len(valid_string) - 1
        
        while l < r:
            if valid_string[l] != valid_string[r]:
                return False
            l += 1
            r -= 1
        return True
        