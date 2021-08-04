from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.target = None
        self.res_paths = []

    def dfs(self, t, cur_path, cur_sum):
        if t is None:
            return
        cur_path.append(t.val)
        cur_sum += t.val
        if cur_sum == self.target and not (t.left or t.right):
            self.res_paths.append(cur_path[:])

        self.dfs(t.left, cur_path, cur_sum)
        self.dfs(t.right, cur_path, cur_sum)

        cur_path.pop()
        cur_sum -= t.val
        return

    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        self.target = targetSum
        self.dfs(root, [], 0)
        return self.res_paths
