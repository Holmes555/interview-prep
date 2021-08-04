# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None
        stack = [node]
        nodes_d = {1: Node(1)}
        visited = set()

        while stack:
            n = stack.pop()
            if n in visited:
                continue
            visited.add(n)
            stack.extend(n.neighbors)
            clone = nodes_d[n.val]
            neighbor_values = [neigh.val for neigh in n.neighbors]
            for i in neighbor_values:
                if i not in nodes_d:
                    cur = Node(i)
                    nodes_d[i] = cur
                clone.neighbors.append(nodes_d[i])

        return nodes_d[1]
