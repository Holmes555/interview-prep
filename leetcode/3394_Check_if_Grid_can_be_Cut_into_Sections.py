from typing import List


class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        vertical_sections = []
        horizontal_sections = []
        v_indexes = set()
        h_indexes = set()
        for x1, y1, x2, y2 in rectangles:
            for i, (y11, y22) in enumerate(vertical_sections):
                if i in v_indexes:
                    continue
                if y11 <= y1 < y22 or y11 < y2 <= y22 or y1 <= y11 and y22 <= y2:
                    y1 = min(y11, y1)
                    y2 = max(y22, y2)
                    v_indexes.add(i)
            for i, (x11, x22) in enumerate(horizontal_sections):
                if i in h_indexes:
                    continue
                if x11 <= x1 < x22 or x11 < x2 <= x22 or x1 <= x11 and x22 <= x2:
                    x1 = min(x11, x1)
                    x2 = max(x22, x2)
                    h_indexes.add(i)

            vertical_sections.append([y1, y2])
            horizontal_sections.append([x1, x2])
        return len(vertical_sections) > 2 + len(v_indexes) or len(horizontal_sections) > 2 + len(h_indexes)


class Solution2:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:

        def checkCuts(rectangles: List[List[int]], dim: int) -> bool:
            rectangles.sort(key=lambda x: x[dim])

            cuts = 0
            finish = rectangles[0][dim + 2]
            for rect in rectangles[1:]:
                if rect[dim] >= finish:
                    cuts += 1
                    finish = rect[dim + 2]
                elif rect[dim + 2] > finish:
                    finish = rect[dim + 2]
            return cuts >= 2

        return checkCuts(rectangles, 0) or checkCuts(rectangles, 1)
