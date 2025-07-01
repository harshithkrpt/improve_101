class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
    
    def addWord(self, word: str):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = set()
        visit = set()
        ROWS, COLS = len(board), len(board[0])
        root = TrieNode()
        for w in words:
            root.addWord(w)

        def backtrack(r,c,node,words):
            if r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c] not in node.children or (r,c) in visit:
                return
            
            visit.add((r,c))
            node = node.children[board[r][c]]
            words += board[r][c]
            if node.isWord:
                res.add(words)
            backtrack(r+1,c,node,words)
            backtrack(r-1,c,node,words)
            backtrack(r,c + 1,node,words)
            backtrack(r,c - 1,node,words)

            visit.remove((r,c))
        
        for r in range(ROWS):
            for c in range(COLS):
                backtrack(r,c,root,"")
        return list(res)