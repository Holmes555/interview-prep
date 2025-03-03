from typing import List


class Solution1:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        l = len(nums)
        max_sum = 0
        raw_sums = [[0 for _ in range(l)] for _ in range(l)]
        for j in range(1, l):
            for i in range(j + 1):
                if i == j:
                    raw_sums[i][j] = nums[j]
                else:
                    raw_sums[i][j] = raw_sums[i - 1][j] - raw_sums[i - 1][i - 1]
                max_sum = max(max_sum, abs(raw_sums[i][j]))

        return max_sum


class Solution2:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        l = len(nums)
        max_sum = 0
        raw_sums = [[] for _ in range(l)]
        raw_sums[0] = nums
        for i in range(1, l):
            for j in range(l - i):
                raw_sums[i].append(raw_sums[i - 1][j] + raw_sums[0][i + j])
                max_sum = max(max_sum, abs(raw_sums[i][j]))

        return max_sum


class Solution3:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        l = len(nums)
        max_sum = 0
        raw_sums = nums.copy()
        for i in range(1, l):
            for j in range(l - i):
                max_sum = max(max_sum, abs(raw_sums[j]))
                raw_sums[j] = raw_sums[j] + nums[i + j]

        return max_sum


class Solution4:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_sum = 0
        raw_sum = 0
        sign = nums[0] >= 0
        sign_changed = False
        for nums in nums:
            raw_sum += nums
            if raw_sum >= 0 and not sign:
                sign = True
                sign_changed = True
            if raw_sum < 0 and sign:
                sign = False
                sign_changed = True
            if sign_changed:
                raw_sum = max_sum + abs(raw_sum)
                raw_sum *= 1 if sign else -1
                sign_changed = False
            max_sum = max(max_sum, abs(raw_sum))

        return max_sum
