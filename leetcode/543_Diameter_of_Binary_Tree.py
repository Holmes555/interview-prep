# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def __init__(self):
        self.mem = {}
        self.c = 0

    def meme(self, a):
        for i in a:
            m = self.mem[i]
            if 'side' in m:
                if m['side'] == 'left':
                    m['l'] = max(self.c - m['c'], m['l'])
                else:
                    m['r'] = max(self.c - m['c'], m['r'])

    def dfs(self, t, a=None):
        if a is None:
            a = []
        if t is None:
            return a
        a.append(id(t))
        self.mem[id(t)] = {'l': 0, 'r': 0, 'c': self.c}
        self.meme(a)
        if t.left is not None:
            self.c += 1
            self.mem[id(t)]['side'] = 'left'
            self.dfs(t.left, a)
            self.c -= 1
        if t.right is not None:
            self.c += 1
            self.mem[id(t)]['side'] = 'right'
            self.dfs(t.right, a)
            self.c -= 1
        return a

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.dfs(root)
        return max([x['l'] + x['r'] for x in self.mem.values()])


class Solution2:
    def __init__(self):
        self.mem = {}
        self.c = 0

    def meme(self, a):
        for i in a:
            m = self.mem[i]
            if 'side' in m:
                if m['side'] == 'left':
                    m['l'] = max(self.c - m['c'], m['l'])
                else:
                    m['r'] = max(self.c - m['c'], m['r'])

    def dfs_w(self, t, a=None):
        if a is None:
            a = []
        l = [(t, None)]
        r = []
        while l or r:
            try:
                t, p = l.pop()
                self.mem[id(t)] = {'l': 0, 'r': 0, 'c': self.c}
                if p is not None:
                    self.mem[id(p)]['side'] = 'left'
            except:
                try:
                    t, p = r.pop()
                    if p is not None:
                        self.c = self.mem[id(p)]['c'] + 1
                        self.mem[id(p)]['side'] = 'right'
                    self.mem[id(t)] = {'l': 0, 'r': 0, 'c': self.c}
                except:
                    return a

            a.append(id(t))
            self.meme(a)
            self.c += 1
            if t.left is not None:
                l.append((t.left, t))
            if t.right is not None:
                r.append((t.right, t))
        return a

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.dfs_w(root)
        return max([x['l'] + x['r'] for x in self.mem.values()])
