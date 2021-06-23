# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def dfs(self, t, a=None, w=1):
        if a is None:
            a = []
        if t is None:
            return a
        if w:
            if t.left is not None:
                self.dfs(t.left, a)
            if t.right is not None:
                self.dfs(t.right, a)
                if t.left is None:
                    a.append(None)
        else:
            if t.right is not None:
                self.dfs(t.right, a, 0)
            if t.left is not None:
                self.dfs(t.left, a, 0)
                if t.right is None:
                    a.append(None)
        a.append(t.val)
        return a

    def isSymmetric(self, root: TreeNode) -> bool:
        return self.dfs(root.left) == self.dfs(root.right, None, 0)
