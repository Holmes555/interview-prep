from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        table = {}
        lc = 0

        for i in nums:
            if i not in table:
                ll = rr = i
                lv = rv = 0
                left = table.get(i - 1, None)
                if left is not None:
                    ll = left['l']
                    lv = left['v']
                right = table.get(i + 1, None)
                if right is not None:
                    rr = right['r']
                    rv = right['v']
                cur_v = lv + rv + 1
                table[i] = {'l': ll, 'r': rr, 'v': cur_v}
                l = table.get(ll, None)
                if l is not None:
                    l['r'] = rr
                    l['v'] = cur_v
                r = table.get(rr, None)
                if r is not None:
                    r['l'] = ll
                    r['v'] = cur_v
                if cur_v > lc:
                    lc = cur_v

        return lc
