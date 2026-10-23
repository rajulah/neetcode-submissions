# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parents = defaultdict()
        parents[root] = None
        pq_found = [0,0]
        def dfs(root, p, q, prevParent):
            if root is None:
                return
            if root == p:
                pq_found[0] = 1
            if root == q:
                pq_found[1] == 1
            # parents[root].append(root)
            if prevParent is not None:
                parents[root] = prevParent
            if pq_found == [1,1]:
                return
            dfs(root.left, p, q, root)
            dfs(root.right, p, q, root)
            return
        dfs(root,p,q, None)
        ancestors = set()
        while p:
            ancestors.add(p)
            print(p.val)
            p = parents[p]
        while q not in ancestors:
            q = parents[q]
        return q

