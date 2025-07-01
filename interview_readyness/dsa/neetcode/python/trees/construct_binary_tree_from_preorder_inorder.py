# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1 : mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :])
        return root



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class OptimalSolution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        hash_store = { val: idx for idx,val in enumerate(inorder) }
        self.pre_idx = 0

        def helper(left, right):
            if left > right:
                return None
            
            val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(val)
            idx = hash_store[val]
            root.left = helper(left, idx - 1)
            root.right = helper(idx + 1, right)

            return root
        return helper(0, len(preorder) - 1)