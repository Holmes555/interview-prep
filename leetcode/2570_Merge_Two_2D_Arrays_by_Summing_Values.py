from typing import List


class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        result_arr = []
        l1 = len(nums1)
        l2 = len(nums2)
        i = j = 0
        while i < l1 and j < l2:
            index1, value1 = nums1[i]
            index2, value2 = nums2[j]
            if index1 > index2:
                result_arr.append([index2, value2])
                j += 1
            elif index1 < index2:
                result_arr.append([index1, value1])
                i += 1
            elif index1 == index2:
                result_arr.append([index1, value1 + value2])
                i += 1
                j += 1
        return result_arr + nums1[i:] + nums2[j:]
