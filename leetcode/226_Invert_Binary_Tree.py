# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def dfs(self, t):
        if t is None:
            return t
        temp = t.left
        t.left = t.right
        t.right = temp

        self.dfs(t.left)
        self.dfs(t.right)

        return t

    def invertTree(self, root: TreeNode) -> TreeNode:
        return self.dfs(root)
