from typing import List


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        operations_map = {
            "++X": 1,
            "X++": 1,
            "--X": -1,
            "X--": -1,
        }
        result = 0

        for operation in operations:
            result += operations_map[operation]
        return result
