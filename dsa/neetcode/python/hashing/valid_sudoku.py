# (row / 3) * 3 + (col / 3)
# it will be a hash map as key with rows -> 0,9 and values as set with no repeatations for rows and columns
# but coming to squares key should be row/3, col /3 of integer values and the values can be same of hash set

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set) # key -> r/3, c/3 

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if (board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r//3, c//3)]):
                    return False
               
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])
        
        return True