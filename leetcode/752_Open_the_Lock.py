from queue import Queue
from typing import List


class Solution:
    def generate_states(self, cur):
        res = []
        arr = [i for i in cur]
        for i in range(4):
            temp = arr[:]
            temp[i] = str((int(temp[i]) + 1) % 10)
            res.append(''.join(temp))
        for i in range(4):
            temp = arr[:]
            temp[i] = str(int(temp[i]) - 1) if temp[i] != '0' else '9'
            res.append(''.join(temp))
        return res

    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        if '0000' in deadends:
            return -1

        def bfs():
            a = Queue()
            a.put('0000')

            while not a.empty():
                t = a.get()
                tn = tree[t]
                if t == target:
                    return tn['m']
                if tn['v'] or t in deadends:
                    continue
                tn['v'] = True
                res = self.generate_states(t)
                tn['neighbours'] = res
                for v in res:
                    if v not in tree:
                        tree[v] = {'v': False, 'm': tn['m'] + 1}
                    else:
                        tempn = tree[v]
                        tempn['m'] = min(tn['m'] + 1, tempn['m'])
                [a.put(v) for v in res]

        tree = {'0000': {'v': False, 'm': 0}}
        bfs()
        node = tree.get(target, None)
        return node['m'] if node else -1
