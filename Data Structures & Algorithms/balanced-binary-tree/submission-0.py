# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        self.balanced = True
        def depth(root):
            if root is None:
                return 0
            left = depth(root.left)
            right = depth(root.right)
            if abs(left - right) > 1:
                self.balanced = False
            return 1 + max(left, right)
        depth(root)
        return self.balanced
