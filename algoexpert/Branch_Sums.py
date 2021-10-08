# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    result = []

    def dfs(t, s):
        if t is None:
            return
        s += t.value
        if t.left is None and t.right is None:
            result.append(s)
            return
        dfs(t.left, s)
        dfs(t.right, s)

    dfs(root, 0)
    return result
