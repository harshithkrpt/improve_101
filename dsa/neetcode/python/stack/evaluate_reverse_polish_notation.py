# Evaluate Reverse Polish Notation
# Solved 
# You are given an array of strings tokens that represents a valid arithmetic expression in Reverse Polish Notation.

# Return the integer that represents the evaluation of the expression.

# The operands may be integers or the results of other operations.
# The operators include '+', '-', '*', and '/'.
# Assume that division between integers always truncates toward zero.

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for ch in tokens:
            if ch not in {"+", "-", "*", "/"}:
                stack.append(int(ch))
            else:
                f = stack.pop()
                s = stack.pop()
                if ch == '+':
                    stack.append(s + f)
                elif ch == '-':
                    stack.append(s - f)
                elif ch == '*':
                    stack.append(s * f)
                elif ch == '/':
                    stack.append(int(s/f))
        return stack[0]
