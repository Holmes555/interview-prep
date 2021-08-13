from queue import Queue
from typing import List


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, newColor: int
    ) -> List[List[int]]:
        n = len(image)
        m = len(image[0])
        q = Queue()
        s = set()
        flood_v = image[sr][sc]

        def add_to_q(i, j):
            if image[i][j] == flood_v and (i, j) not in s:
                q.put((i, j))
                s.add((i, j))
                return True
            return False

        def check_neighbours(i, j):
            if j != 0:
                add_to_q(i, j - 1)
            if i != 0:
                add_to_q(i - 1, j)
            if j != m - 1:
                add_to_q(i, j + 1)
            if i != n - 1:
                add_to_q(i + 1, j)

        add_to_q(sr, sc)

        while not q.empty():
            el = q.get()
            image[el[0]][el[1]] = newColor
            check_neighbours(*el)

        return image
