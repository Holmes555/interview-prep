def nodeDepths(root):
    def bfs(r):
        result = 0
        a = [(r, 0)]

        while a:
            t = a.pop()
            if t[0] is None:
                continue
            result += t[1]
            a.append((t[0].left, t[1] + 1))
            a.append((t[0].right, t[1] + 1))

        return result

    return bfs(root)


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
