class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_l = 0
        substr = ''
        for c in s:
            if c in substr:
                substr = substr[substr.index(c) + 1 :]
            substr += c
            if len(substr) > max_l:
                max_l = len(substr)
        return max_l
