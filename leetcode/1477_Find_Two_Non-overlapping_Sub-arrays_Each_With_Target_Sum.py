from typing import List


class Solution1:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        def check_sum(new_arr):
            n = len(new_arr)
            sub_arrays_l = []
            overlapping = -1

            for i in range(n):
                current_sum = 0
                if i > overlapping:
                    overlapping = -1
                for j in range(i, n):
                    current_sum += new_arr[j]
                    if current_sum == target:
                        length = j - i + 1
                        if overlapping != -1:
                            if sub_arrays_l[-1] > length:
                                sub_arrays_l[-1] = length
                                overlapping = j
                        else:
                            sub_arrays_l.append(length)
                            overlapping = j
                        break
                    if current_sum > target:
                        break

            sub_arrays_l.sort()
            return sub_arrays_l[0] + sub_arrays_l[1] if len(sub_arrays_l) >= 2 else -1

        result1 = check_sum(arr)
        result2 = check_sum(arr[::-1])
        if result1 == -1 or result2 == -1:
            return max(result1, result2)
        return min(result1, result2)


class Solution2:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        prefix_sum = {0: -1}
        current_sum = 0
        min_length = [float('inf')] * n
        result = float('inf')
        min_len = float('inf')

        for i in range(n):
            current_sum += arr[i]
            if current_sum - target in prefix_sum:
                start_index = prefix_sum[current_sum - target] + 1
                length = i - start_index + 1
                if start_index > 0 and min_length[start_index - 1] != float('inf'):
                    result = min(result, length + min_length[start_index - 1])
                min_len = min(min_len, length)
            min_length[i] = min_len
            prefix_sum[current_sum] = i

        return result if result != float('inf') else -1
