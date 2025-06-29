class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        col = set()
        pDiag = set() # r + c
        nDiag = set() # r -c 
        
        board = [["."] * n for i in range(n)]
        def _queen(row):
            if row == n:
                c = ["".join(row) for row in board]
                res.append(c)
                return
            for c in range(n):
                if c in col or (row + c) in pDiag or (row - c) in nDiag:
                    continue
                col.add(c)
                pDiag.add(row+c)
                nDiag.add(row-c)
                board[row][c] = 'Q'
                _queen(row + 1)
                col.remove(c)
                pDiag.remove(row+c)
                nDiag.remove(row-c)
                board[row][c] = '.'
        _queen(0)
        return res
