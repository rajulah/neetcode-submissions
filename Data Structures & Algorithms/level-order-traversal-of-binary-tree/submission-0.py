# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        queue = [root]
        nextQueue = []
        level =[]
        result = []
        while queue != []:
            for node in queue:
                level.append(node.val)
                if node.left:
                    nextQueue.append(node.left)
                if node.right:
                    nextQueue.append(node.right)
            
            queue = nextQueue
            result.append(level)
            nextQueue = []
            level = []
        return result
