from typing import List


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        frequency = {}
        max_freq = 0
        count_max_freq = 0

        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1
            if frequency[num] > max_freq:
                max_freq = frequency[num]
                count_max_freq = max_freq
            elif frequency[num] == max_freq:
                count_max_freq += max_freq

        return count_max_freq
