class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # calculate rows and cols len
        ROWS, COLS = len(board), len(board[0])
        # path value of tuple as set with r,c
        path = set()
        # inner function with conditions
        def backtrack(r, c, i):
        # path length matches word length return true
            if len(word) == len(path):
                return True
        # lower bound
        # upper bound
        # word matching not matching 
        # if value is already in path -> visited node
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or word[i] != board[r][c] or (r,c) in path:
                return False 
        # add the node to path
            path.add((r,c))
            # find the same recursively in all directions 
            res = backtrack(r+1, c, i + 1) or backtrack(r, c+1, i+1) or backtrack(r-1,c, i+1) or backtrack(r,c-1,i + 1)
            # remove the path
            path.remove((r,c))
            # return res of all four directions
            return res
    
    # now run the recursive backtrack for every node as starting 
        for r in range(ROWS):
            for c in range(COLS):
                if backtrack(r,c,0):
                    return True
        # return false if all fails
        return False