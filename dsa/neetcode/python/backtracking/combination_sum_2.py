class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backtrack(idx, cur, total):
            if target == total:
                res.append(list(cur))
                return
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                if candidates[i] + total > target:
                    return
                cur.append(candidates[i])
                backtrack(i + 1, cur, total + candidates[i])
                cur.pop()
        backtrack(0, [], 0)
        return res