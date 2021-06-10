from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = []
        i = 0

        while True:
            for j, s in enumerate(strs):
                try:
                    if j == 0:
                        prefix.append(s[i])
                    else:
                        if prefix[i] != s[i]:
                            return ''.join(prefix[:-1])
                except:
                    return ''.join(prefix[:i])
            i += 1
