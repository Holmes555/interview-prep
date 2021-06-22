from typing import List


class Solution1:
    def __init__(self):
        self.l = 0
        self.k = 0
        self.c = 0

    def remove(self, i, arr):
        arr[i - self.c :] = arr[i:]

    def removeDuplicates(self, nums: List[int]) -> int:
        self.l = len(nums)
        i = 1

        while i < self.l - self.k:
            if nums[i - 1] == nums[i]:
                self.c += 1
            elif self.c > 0:
                self.remove(i, nums)
                i -= self.c
                self.k += self.c
                self.c = 0
            i += 1

        for _ in range(self.c):
            nums.pop()


class Solution2:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = len(nums)
        if l < 2:
            return l

        i = k = 0
        for j in range(1, l):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
            else:
                k += 1
        return l - k
