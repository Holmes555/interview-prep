from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        self._nums = nums
        self._memo = {}
        self._changes = {}

    def _check_changes(self, left: int, right: int) -> int:
        res = 0
        for key in self._changes.keys():
            if left <= key < right:
                res += self._changes.pop(key)
        return res

    def _check_memo(self, left: int, right: int):
        res = 0
        l = r = -1
        for key in self._memo.keys():
            if key[0] >= left and key[1] <= right:
                diff = key[1] - key[0]
                if diff > res:
                    res = diff
                    l, r = key[0], key[1]
        return l, r

    def _resum_memo(self, index, old_v, new_v):
        for key in self._memo.keys():
            if key[0] <= index < key[1]:
                self._memo[key] += new_v - old_v

    def update(self, index: int, val: int) -> None:
        self._changes[index] = (self._nums[index], val)
        self._nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        if left == right:
            return self._nums[left]
        right = right + 1
        if (left, right) in self._memo:
            res = self._check_changes(left, right)
            s = self._memo[(left, right)] + res
            self._memo[(left, right)] = s
            return s
        else:
            l, r = self._check_memo(left, right)
            if l != -1 and r != -1:
                sl = sum(self._nums[left:l])
                self._memo[(left, l)] = sl
                sr = sum(self._nums[r:right])
                self._memo[(r, right)] = sr
                s = sl + self._memo[(l, r)] + sr
                self._memo[(left, right)] = s
                return s

        # if left in self._memo:
        #     if right in self._memo[left]:
        #         res = self._check_changes(left, right)
        #         s = self._memo[left][right] + res
        #         self._memo[left][right] = s
        #         return s
        #     i = self._check_memo(left, right, True)
        #     s1 = sum(self._nums[i:right])
        #     self._memo[i], right)] = s1
        #     s = self._memo[(left, i)] + 1
        #     self._memo[(left, right)] = s
        #     return s
        # if right in self._memo:
        #     if right in self._memo[left]:
        #         res = self._check_changes(left, right)
        #         s = self._memo[left][right] + res
        #         self._memo[left][right] = s
        #         return s
        #     i = self._check_memo(left, right, True)
        #     s1 = sum(self._nums[i:right])
        #     self._memo[(i, right)] = s1
        #     s = self._memo[(left, i)] + 1
        #     self._memo[(left, right)] = s
        #     return s
        s = sum(self._nums[left:right])
        self._memo[(left, right)] = s
        return s


class NumArray1:
    def __init__(self, nums: List[int]):
        self._nums = nums
        self._memo = {}

    def _resum_memo(self, index, old_v, new_v):
        for key in self._memo.keys():
            if key[0] <= index < key[1]:
                self._memo[key] += new_v - old_v

    def update(self, index: int, val: int) -> None:
        self._resum_memo(index, self._nums[index], val)
        self._nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        if left == right:
            return self._nums[left]
        right = right + 1
        if (left, right) in self._memo:
            return self._memo[(left, right)]
        s = sum(self._nums[left:right])
        self._memo[(left, right)] = s
        return s


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
