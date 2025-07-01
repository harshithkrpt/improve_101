# Use Backtracking to explore all valid combinations by maintaining:

# open → number of ( used

# close → number of ) used

# Only add a ) if close < open.

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(ans, open_p, close_p):
            if len(ans) == 2 * n:
                result.append(ans)
                return
            if open_p < n:
                backtrack(ans + "(", open_p + 1, close_p)
            if close_p < open_p:
                backtrack(ans + ")", open_p, close_p + 1)

        backtrack("", 0, 0)
        return result
        
