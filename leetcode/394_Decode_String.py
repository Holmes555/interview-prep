import string


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        cur = {}
        num = []
        res = []
        for c in s:
            if c in string.digits:
                num.append(c)
            elif c == '[':
                if cur:
                    stack.append(cur)
                cur = {'count': int(''.join(num)), 'chars': []}
                num = []
                continue
            elif c == ']':
                cur_s = ''.join(cur['chars']) * int(cur['count'])
                if stack:
                    stack[-1]['chars'].append(cur_s)
                    cur = stack.pop()
                else:
                    res.append(cur_s)
                    cur = {}
            else:
                if cur:
                    cur['chars'].append(c)
                else:
                    res.append(c)
        return ''.join(res)
