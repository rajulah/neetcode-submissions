# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # input -> 2 binary trees
        # outout -> bool - if they are equivalent
        # equivalent -> exact same structure and values.

        # clarifications
        # are values integers? doesn't matter cz we are doing val == val comparison
        # can any root given be empty? we will handle empty case
        # Let me use recursive dfs here

        def dfs(p, q):
            if p is None and q is None:
                return True
            if not p or not q:
                return False

            if p.val != q.val:
                return False
            
            return dfs(p.left, q.left) and dfs(p.right, q.right)

        return dfs(p, q)
                                




