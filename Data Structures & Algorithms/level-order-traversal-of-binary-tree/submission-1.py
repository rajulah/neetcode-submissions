# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # given -> root
        # return level order traversal
        # we will utilize two queues, one to hold current level, and one to hold next level that we can iterate in next iteration
        result = []
        if root is None:
            return []
        queue = [root]
        nextQueue = []
        level = []
        while queue:
            for node in queue:
                level.append(node.val)
                if node.left:
                    nextQueue.append(node.left)
                if node.right:
                    nextQueue.append(node.right)
            result.append(level)
            level = []
            queue = nextQueue
            nextQueue = []
        return result