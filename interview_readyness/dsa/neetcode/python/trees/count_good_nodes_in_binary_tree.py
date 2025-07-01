# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.count = 0
        def dfs(cur, maxi):
            if not cur:
                return
            if cur.val >= maxi:
                maxi = cur.val
                self.count += 1
            dfs(cur.left, maxi)
            dfs(cur.right, maxi)
        dfs(root, -100)
        return self.count