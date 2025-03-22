from typing import List


class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        edges_dict = {i: {i} for i in range(n)}
        for i, j in edges:
            edges_dict[i].add(j)
            edges_dict[j].add(i)
        visited = set()
        components = 0
        for k, v in edges_dict.items():
            if k not in visited:
                visited.add(k)
                is_connected = True
                for i in v:
                    visited.add(i)
                    if v != edges_dict[i]:
                        is_connected = False
                if is_connected:
                    components += 1

        return components
