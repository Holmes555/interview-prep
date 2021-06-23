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
        if t.left is not None:
            self.dfs(t.left, a)
        a.append(t.val)
        if t.right is not None:
            self.dfs(t.right, a)
        return a

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        return self.dfs(root)
