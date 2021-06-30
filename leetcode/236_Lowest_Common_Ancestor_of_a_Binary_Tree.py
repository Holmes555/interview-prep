# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.lca = None
        self.p = None
        self.q = None

    def dfs(self, t):
        if t is None:
            return 0
        lca = [0, 0, 0]
        if t.val == self.p.val or t.val == self.q.val:
            lca[0] = 1
        lca[1] = self.dfs(t.left)
        lca[2] = self.dfs(t.right)
        if sum(lca) > 1:
            self.lca = t
        return max(lca)

    def lowestCommonAncestor(
        self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode'
    ) -> 'TreeNode':
        self.p = p
        self.q = q
        self.dfs(root)
        return self.lca
