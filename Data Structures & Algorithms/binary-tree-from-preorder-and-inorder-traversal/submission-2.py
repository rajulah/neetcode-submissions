# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indexes = {}
        for i in range(len(inorder)):
            indexes[inorder[i]] = i
        
        self.preIndex = 0

        def buildTree(left, right):
            if left > right:
                return None
            root = TreeNode(preorder[self.preIndex])
            mid = indexes[preorder[self.preIndex]]
            self.preIndex += 1

            root.left = buildTree(left, mid - 1)
            root.right = buildTree(mid + 1, right)
            return root
        return buildTree(0, len(inorder) - 1)













