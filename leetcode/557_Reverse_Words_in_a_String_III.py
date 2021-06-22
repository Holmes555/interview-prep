class Solution:
    def reverseWords(self, s: str) -> str:
        arr = [word[::-1] for word in s.split()]
        return ' '.join(arr)
