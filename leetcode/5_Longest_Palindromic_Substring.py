class Solution:
    def palLenght(self, s: str) -> int:
        if s == s[::-1]:
            return len(s)
        else:
            return 0

    def indexes(self, s: str, c: str) -> list:
        lst = []
        j = 0
        while True:
            try:
                i = s.index(c)
                lst.append(i + j)
                s = s[i + 1 :]
                j += i + 1
            except ValueError:
                break
        return lst

    def longestPalindrome(self, s: str) -> str:
        max_l = 0
        max_s = None
        for i, c in enumerate(s):
            for j in self.indexes(s, c):
                l = self.palLenght(s[i : j + 1])
                if l > max_l:
                    max_l = l
                    max_s = s[i : j + 1]
        return max_s

    # def longestPalindrome(self, s: str) -> str:
    #     if len(s) == 1:
    #         return s
    #     max_l = 0
    #     max_s = None
    #     for i, c in enumerate(s):
    #         for j in range(len(s) - 1, 0, -1):
    #             l = self.palLenght(s[i:j + 1])
    #             if l > max_l:
    #                 max_l = l
    #                 max_s = s[i:j + 1]
    #                 break
    #         if max_l > len(s) - i - 2:
    #             return max_s
    #     return max_s
