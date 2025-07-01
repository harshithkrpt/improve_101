# Valid Parentheses
# you are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

# The input string s is valid if and only if:

# Every open bracket is closed by the same type of close bracket.
# Open brackets are closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
# Return true if s is a valid string, and false otherwise.

# Input: s = "[]"

# Output: true

# Input: s = "([{}])"

# Output: true


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        related = {
            '}': '{',
            ']': '[',
            ')': '('
        }

        for ch in s:
            if ch == '{' or ch == '(' or ch == '[':
                stack.append(ch)
            else:
                if(len(stack)):
                    popped = stack.pop()
                    if related[ch] != popped:
                        return False
                else:
                    return False
        
        return len(stack) == 0