# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        self.val = X
        self.left = None
        self.right = None

        if root is None:
            return False
        if root.left is None or root.right is None:
            return False
        return root.val == root.left.val + root.right.val