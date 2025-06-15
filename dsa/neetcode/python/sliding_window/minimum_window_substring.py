# ✅ High-Level Idea:
# We slide a window over s using two pointers (l, r) and keep track of the character counts inside the window. Once the window contains all characters from t in the required frequencies, we try to shrink it to find the minimum valid window.
 class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": 
            return ""
        window = {}
        countT = {}
        # Calculate the Need Hash Map
        for ch in t:
            countT[ch] = 1 + countT.get(ch, 0)
        have, need = 0, len(countT)  
        res, resLen = [-1,-1], float("infinity")
        l = 0
        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r], 0)
    
            if s[r] in countT and countT[s[r]] == window[s[r]]:
                have += 1
            
            while have == need:
                if (r - l + 1) < resLen:
                    resLen = (r - l + 1)
                    res = [l,r]
                window[s[l]] -= 1

                # check if removing this is reducing the have count
                if s[l] in countT and  window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        
        if resLen != float("infinity"):
            l, r = res
            return s[l:r + 1]
        return ""
            

        