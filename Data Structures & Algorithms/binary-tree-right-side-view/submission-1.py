# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        queue = [root]
        nextQueue = []
        # level = []
        result = []
        while queue != []:
            result.append(queue[-1].val)
            for node in queue:
                # level.append(node.val)
                if node.left:
                    nextQueue.append(node.left)
                if node.right:
                    nextQueue.append(node.right)
            # if len(level)>0:
            #     result.append(level[-1])
            # level = []
            queue = nextQueue
            nextQueue = []
        return result