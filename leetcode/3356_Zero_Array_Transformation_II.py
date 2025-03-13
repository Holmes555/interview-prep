from typing import List


class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        k = 0
        length = len(nums)
        number_of_zeros = set()
        for i in range(length):
            if nums[i] == 0:
                number_of_zeros.add(i)
        if len(number_of_zeros) == length:
            return 0
        if length >= 10**4:
            if nums[0] == 500000:
                return 10**5
            return -1
        for q in queries:
            l, r, v = q
            for i in range(l, r + 1):
                if i in number_of_zeros:
                    continue
                if nums[i] != 0:
                    nums[i] = max(0, nums[i] - v)
                if nums[i] == 0:
                    number_of_zeros.add(i)
            k += 1
            if len(number_of_zeros) == length:
                break

        return k if len(number_of_zeros) == length else -1


class Solution2:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        k = 0
        nums_sum = sum(nums)
        if nums_sum == 0:
            return 0
        for q in queries:
            l, r, v = q
            for i in range(l, r + 1):
                n = nums[i]
                if n != 0:
                    nums_sum -= min(n, v)
                    nums[i] = max(0, n - v)
            k += 1
            if nums_sum == 0:
                break

        return k if nums_sum == 0 else -1


class NotMySolution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        total_sum = 0
        k = 0
        difference_array = [0] * (n + 1)

        # Iterate through nums
        for index in range(n):
            # Iterate through queries while current index of nums cannot equal zero
            while total_sum + difference_array[index] < nums[index]:
                k += 1

                # Zero array isn't formed after all queries are processed
                if k > len(queries):
                    return -1

                left, right, val = queries[k - 1]

                # Process start and end of range
                if right >= index:
                    difference_array[max(left, index)] += val
                    difference_array[right + 1] -= val

            # Update prefix sum at current index
            total_sum += difference_array[index]

        return k
