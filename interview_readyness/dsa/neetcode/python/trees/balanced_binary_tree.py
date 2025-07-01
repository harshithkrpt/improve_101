# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.res = True

        def dfs(cur):
            if not cur:
                return 0
            
            l = 1 + dfs(cur.left) if cur.left else 0
            r = 1 + dfs(cur.right) if cur.right else 0

            maxi = max(l,r)
            mini = min(l,r)
            if maxi - mini > 1:
                self.res = False
            return max(l,r)
        dfs(root)
        return self.res
            

