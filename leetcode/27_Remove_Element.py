from typing import List


class Solution:
    def __init__(self):
        self.l = 0
        self.k = 1

    def remove(self, i, arr):
        for j in range(i, self.l - self.k):
            arr[j] = arr[j + 1]

    def removeElement(self, nums: List[int], val: int) -> int:
        self.l = len(nums)
        i = 0

        while i <= self.l - self.k:
            if nums[i] == val:
                self.remove(i, nums)
                i -= 1
                self.k += 1
                nums.pop()
            i += 1
        # nums = nums[:self.l-self.k]
        # nums.remove(val)
        # return len(nums)


class Solution2:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = len(nums)
        if l == 0:
            return 0

        i = 0
        j = l - 1

        while i <= j:
            if nums[i] == val and nums[j] != val:
                nums[i], nums[j] = nums[j], nums[i]

            if nums[i] != val:
                i += 1
            if nums[j] == val:
                j -= 1

        return j + 1
