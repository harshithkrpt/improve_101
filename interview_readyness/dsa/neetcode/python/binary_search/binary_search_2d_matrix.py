from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        tR = 0
        bR = len(matrix) - 1

        while tR <= bR:
            mR = (tR + bR) // 2
            n = len(matrix[mR])
            if matrix[mR][0] <= target and matrix[mR][n-1] >= target:
                # binary search
                lp, rp = 0, n - 1
                while lp <= rp:
                    mP = (lp + rp) // 2
                    if matrix[mR][mP] == target:
                        return True
                    elif matrix[mR][mP] < target:
                        lp = mP + 1
                    else:
                        rp = mP - 1
                return False
                        
            elif matrix[mR][0] < target:
                tR = mR + 1
            else:
                bR = mR - 1

        return False