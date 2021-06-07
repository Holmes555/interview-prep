import statistics
from typing import List


class Solution:
    def findMedianSortedArrays(
        self, nums1: List[int], nums2: List[int]
    ) -> float:
        res = sorted(nums1 + nums2)
        return statistics.median(res)


class Solution2:
    def findMedianSortedArrays(
        self, nums1: List[int], nums2: List[int]
    ) -> float:
        res = sorted(nums1 + nums2)
        l = len(res)
        if l % 2 == 0:
            l = int(l / 2)
            return (res[l - 1] + res[l]) / 2.0
        else:
            l = int(l / 2)
            return res[l]
