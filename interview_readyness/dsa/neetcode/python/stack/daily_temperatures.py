# Use a monotonically decreasing stack of indices.
# At each index i, while stack is not empty and T[i] > T[stack[-1]], 
# pop from stack and update the answer for the popped index as i - prev_index.

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        
        if not temperatures:
            return []
        
        for i in range(len(temperatures)):
            # current temperature is less then or equal to current stack
            if not stack or temperatures[i] <= temperatures[stack[-1]]:
                stack.append(i)
            else:
                while stack and temperatures[stack[-1]] < temperatures[i]:
                    p_idx = stack.pop()
                    result[p_idx] = i - p_idx
                stack.append(i)
        
        return result
        