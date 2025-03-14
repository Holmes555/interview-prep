from typing import List


class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        sum_candies = sum(candies)
        max_pile = max(candies)
        max_candies = sum_candies // k
        if max_candies == 0:
            return 0

        left = 1
        right = min(max_pile, max_candies)
        last_max = 1
        while left < right:
            mid = (left + right) // 2
            piles = 0
            for c in candies:
                piles += c // mid
            if piles < k:
                right = mid
            else:
                last_max = mid
                left = mid + 1

        piles = 0
        for c in candies:
            piles += c // left
        if piles >= k:
            return left
        return last_max
