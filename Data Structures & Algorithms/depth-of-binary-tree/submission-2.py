# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # input -> root of a binary tree
        # output -> depth of the binary tree
        # depth -> number of nodes from root to leaf node -> longest length
        if root is None:
            return 0
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        max_depth = 1 + max(left_depth, right_depth)
        return max_depth



        