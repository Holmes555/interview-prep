# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def dfs(self, t):
        if t is None:
            return 0
        if t.left is None and t.right is None:
            return 1

        a = self.dfs(t.left)
        b = self.dfs(t.right)

        return max(a, b) + 1

    def maxDepth(self, root: TreeNode) -> int:
        return self.dfs(root)
