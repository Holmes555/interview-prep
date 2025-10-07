from typing import List


class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        res = [-2] * n
        full_lakes = {}
        dry_days = []

        for i, lake in enumerate(rains):
            if lake == 0:
                dry_days.append(i)
                res[i] = 1
            else:
                if lake in full_lakes:
                    for day in dry_days:
                        if day > full_lakes[lake]:
                            res[day] = lake
                            dry_days.remove(day)
                            full_lakes.pop(lake)
                            break
                    else:
                        return []

                full_lakes[lake] = i
                res[i] = -1

        return res
