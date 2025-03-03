from typing import List


class Solution:

    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = int((l + r) / 2)
            if nums[m] == target:
                return m
            if nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        return -1

    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        max_len = 0
        l = len(arr)
        checked = {}
        num_dict = {k: i for i, k in enumerate(arr)}

        for i in range(l - max_len - 1):
            for j in range(i + 1, l - max_len - 1):
                temp_len = 0
                a = i
                b = j
                if (a, b) in checked:
                    if checked[(a, b)] >= arr[-1 - max_len]:
                        if b == a + 1:
                            return max_len + 2 if max_len > 0 else 0
                        break
                    continue
                while True:
                    value = arr[a] + arr[b]
                    checked[(a, b)] = value
                    k = num_dict.get(value)
                    if k:
                        temp_len += 1
                        a = b
                        b = k
                        if k >= l - max_len - 1 + temp_len:
                            max_len = max(max_len, temp_len)
                            break
                    else:
                        max_len = max(max_len, temp_len)
                        break

        return max_len + 2 if max_len > 0 else 0

    def lenLongestFibSubseq2(self, arr: List[int]) -> int:
        fib = [set()]
        max_len = 0
        l = len(arr)
        counter = 0
        checked = set()
        i = 0
        temp_max = 0

        while i < l - temp_max - 1:
            j = i + 1
            while j < l - temp_max - 1:
                a = i
                b = j
                if (a, b) in checked:
                    continue
                while True:
                    value = arr[a] + arr[b]
                    checked.add((a, b))
                    k = self.search(arr, value)
                    if k != -1:
                        fib[counter].add(value)
                        a = b
                        b = k
                        if k >= l - temp_max - 1:
                            max_len = max(max_len, len(fib[counter]))
                            temp_max = max_len + 2 if max_len > 0 else 0
                            counter += 1
                            fib.append(set())
                            break
                    else:
                        max_len = max(max_len, len(fib[counter]))
                        temp_max = max_len + 2 if max_len > 0 else 0
                        counter += 1
                        fib.append(set())
                        break
                j += 1
            i += 1

        return temp_max
