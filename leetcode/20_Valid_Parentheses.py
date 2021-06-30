class Solution:
    def isValid(self, s: str) -> bool:
        open_p = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for c in s:
            if c in open_p:
                stack.append(open_p[c])
            else:
                if not stack or c != stack.pop():
                    return False
        return not stack
