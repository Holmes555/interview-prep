from typing import List


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        res = 0

        for w in words:
            i = 0
            for c in w:
                try:
                    i += s[i:].index(c) + 1
                except ValueError:
                    break
            else:
                res += 1

        return res
