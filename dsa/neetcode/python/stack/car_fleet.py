# this also uses monotinically decreasing stack
# sort cars by position -> descending 
# calculate time of each car -> time  = (target - pos[i]) / speed[i]

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p,s] for p,s in zip(position, speed)]
        # sort based on position as it is the first element
        s_pair = sorted(pair, reverse=True)

        stack = []
        for p,s in s_pair:
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        print(stack)
        return len(stack)