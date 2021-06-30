from typing import List


class Solution:
    def __init__(self):
        self.d = {}
        self.s = set()
        self.c = None
        self.k = set()

    def rec(self, k, target):
        if target < self.c[-1]:
            return self.d.get(target, set())
        for i in self.c[k:]:
            if i > target:
                return self.rec(k + 1, target)
            if target not in self.d:
                self.d[target] = set()
            if i == target:
                self.d[target].add((i,))
            else:
                ad = target - i
                if ad in self.s:
                    self.d[target].add((i, ad))
                b = self.rec(k, ad)
                if b:
                    a = self.rec(k, i)
                    if a:
                        for n in a:
                            for m in b:
                                self.d[target].add((*n, *m))
        return self.d.get(target, set())

    def combinationSum(
        self, candidates: List[int], target: int
    ) -> List[List[int]]:
        self.s = set(candidates)
        self.c = sorted(candidates, reverse=True)
        res = self.rec(0, target)
        res = set(tuple(sorted(x)) for x in res)
        return res


class Solution2:
    def __init__(self):
        self.d = {}
        self.s = set()
        self.c = None
        self.k = set()

    def rec(self, k, target):
        if (k, target) not in self.k:
            self.k.add((k, target))
        else:
            return self.d.get(target, set())
        if target < self.c[-1]:
            return self.d.get(target, set())
        for i in self.c[k:]:
            if i > target:
                return self.rec(k + 1, target)
            if target not in self.d:
                self.d[target] = set()
            if i == target:
                self.d[target].add((i,))
            else:
                ad = target - i
                if ad < self.c[-1]:
                    continue
                if ad in self.s:
                    self.d[target].add((i, ad))
                b = self.rec(k, ad)
                if b:
                    a = self.rec(k, i)
                    if a:
                        for n in a:
                            for m in b:
                                self.d[target].add((*n, *m))
        return self.d.get(target, set())

    def combinationSum(
        self, candidates: List[int], target: int
    ) -> List[List[int]]:
        self.s = set(candidates)
        self.c = sorted(candidates, reverse=True)
        res = self.rec(0, target)
        res = set(tuple(sorted(x)) for x in res)
        return res
