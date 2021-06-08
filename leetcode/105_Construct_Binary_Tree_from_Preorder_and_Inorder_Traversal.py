# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.t = {}

    def rec(self, t, lr, rr):
        i, n = t
        ll = len(lr)
        rl = len(rr)
        if ll > 0:
            l = lr[0]
            li, ln = self.t[l]
            new_i = (i - li) - 1
            if new_i == 0:
                n.left = self.rec((li, ln), lr[1:], [])
            else:
                n.left = self.rec((li, ln), lr[1:-new_i], lr[-new_i:])
                # n.left = self.rec((li, ln), lr[1:i-li-1], lr[i-li-1:])
        if rl > 0:
            r = rr[0]
            ri, rn = self.t[r]
            n.right = self.rec((ri, rn), rr[1 : ri - i], rr[ri - i :])
        return n

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        for i, v in enumerate(inorder):
            self.t[v] = (i, TreeNode(v))

        r = preorder[0]
        ri, rn = self.t[r]

        return self.rec((ri, rn), preorder[1 : ri + 1], preorder[ri + 1 :])
