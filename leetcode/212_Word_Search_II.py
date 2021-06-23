from typing import List


class Solution:
    def __init__(self):
        self.v = set()
        self.n = 0
        self.m = 0

    def rec(self, coords, word, board):
        if len(word) == 0:
            return True
        i, j = coords
        if i - 1 >= 0 and (i - 1, j) not in self.v:
            c = board[i - 1][j]
            if c == word[0]:
                self.v.add((i - 1, j))
                t = self.rec((i - 1, j), word[1:], board)
                if t:
                    return t
                self.v.remove((i - 1, j))
        if j - 1 >= 0 and (i, j - 1) not in self.v:
            c = board[i][j - 1]
            if c == word[0]:
                self.v.add((i, j - 1))
                t = self.rec((i, j - 1), word[1:], board)
                if t:
                    return t
                self.v.remove((i, j - 1))
        if i + 1 < self.n and (i + 1, j) not in self.v:
            c = board[i + 1][j]
            if c == word[0]:
                self.v.add((i + 1, j))
                t = self.rec((i + 1, j), word[1:], board)
                if t:
                    return t
                self.v.remove((i + 1, j))
        if j + 1 < self.m and (i, j + 1) not in self.v:
            c = board[i][j + 1]
            if c == word[0]:
                self.v.add((i, j + 1))
                t = self.rec((i, j + 1), word[1:], board)
                if t:
                    return t
                self.v.remove((i, j + 1))

        return False

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        cells = {}

        self.n = len(board)
        self.m = len(board[0])

        for i in range(self.n):
            for j in range(self.m):
                a = board[i][j]
                if a not in cells:
                    cells[a] = []
                cells[a].append((i, j))

        res = []

        for word in words:
            self.v = set()
            s = set(word)
            if any(k not in cells for k in s):
                continue
            c = word[0]
            if c not in cells:
                continue
            for coords in cells[c]:
                self.v.add(coords)
                t = self.rec(coords, word[1:], board)
                if t:
                    res.append(word)
                    break
                self.v.remove(coords)

        return res
