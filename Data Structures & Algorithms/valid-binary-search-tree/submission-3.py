# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, min_bound, max_bound):
            if not root:
                return True
            if root.val <= min_bound or root.val >= max_bound:
                return False
            
            return dfs(root.left, min_bound, root.val) and dfs(root.right, root.val, max_bound)
        return dfs(root, float('-inf'), float('inf'))