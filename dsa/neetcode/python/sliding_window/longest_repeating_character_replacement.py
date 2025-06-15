# You are given a string s consisting of only uppercase english characters and an integer k. You can choose up to k characters of the string and replace them with any other uppercase English character.

# After performing at most k replacements, return the length of the longest substring which contains only one distinct character.

# O(26 * N)
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        count = {}
        for r in range(len(s)):
            # Calculate the Count
            count[s[r]] = 1 + count.get(s[r], 0)
            # make sure it is valid string
            while ((r - l + 1) - max(count.values())) > k:
                # Decrement the count if 
                count[s[l]] -= 1
                l += 1
            # Store the Maximum Resukt
            res = max(res, r - l + 1)

            
        return res


# O(N) as we are storing the max value
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        count = {}
        maxf = 0
        for r in range(len(s)):
            # Calculate the Count
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])
            # make sure it is valid string
            while ((r - l + 1) - maxf) > k:
                # Decrement the count if 
                count[s[l]] -= 1
                l += 1
            # Store the Maximum Resukt
            res = max(res, r - l + 1)
        return res