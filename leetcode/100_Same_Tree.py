# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def dfs(self, t, a=None):
        if a is None:
            a = []
        if t is None:
            return a
        a.append(t.val)
        if t.left is not None:
            self.dfs(t.left, a)
        if t.right is not None:
            if t.left is None:
                a.append(None)
            self.dfs(t.right, a)
        return a

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        a = self.dfs(p)
        b = self.dfs(q)
        return a == b
