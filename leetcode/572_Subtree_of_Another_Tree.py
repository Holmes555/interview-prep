# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def bfs(self, t, c):
        a = [t]

        while a:
            t = a.pop()
            if t is None:
                continue
            if str(t) == str(c):
                return True
            a.append(t.left)
            a.append(t.right)

        return False

    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        return str(subRoot) in str(root)


class Solution2:
    def dfs(self, t, a=None):
        if a is None:
            a = []
        if t is None:
            return a
        a.append(str(t.val))
        if t.left is not None:
            self.dfs(t.left, a)
            a.append('l')
        if t.right is not None:
            if t.left is None:
                a.append('None')
            self.dfs(t.right, a)
            a.append('r')
        return a

    def list_in(self, a, b):
        l1 = len(a)
        l2 = len(b)
        node = a.count('l') - a.count('r')
        for i in range(l2 - l1 + 1):
            if a == b[i : i + l1]:
                if l1 == 1 and i + l1 + 1 < l2:
                    if b[i + l1] == 'l' or b[i + l1] == 'r':
                        return True
                    else:
                        continue
                if i + l1 + 1 >= l2:
                    return True
                if not node:
                    return True
                if node and (b[i + l1] == 'l' or b[i + l1] == 'r'):
                    return True
        return False

    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        a = self.dfs(root)
        b = self.dfs(subRoot)
        return self.list_in(b, a)
