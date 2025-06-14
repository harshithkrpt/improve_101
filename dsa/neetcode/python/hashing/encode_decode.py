# Encode and Decode Strings
# Solved 
# Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

# Please implement encode and decode

class Solution:

    def encode(self, strs: List[str]) -> str:
        r_str = ""
        for s in strs:
            r_str += "{}#{}".format(len(s), s) 
        return r_str


    def decode(self, s: str) -> List[str]:
        t_s = s
        res = []
        while len(t_s):
            index_of_hash = t_s.find("#")
            count = int(t_s[0:index_of_hash])
            t_s = t_s[index_of_hash + 1:]
            value = t_s[0:count]
            res.append(value)
            t_s = t_s[count:]
        return res
        
