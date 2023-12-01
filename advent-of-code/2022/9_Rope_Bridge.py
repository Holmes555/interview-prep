import dataclasses
from typing import List

input_path = 'input/9_Rope_Bridge.txt'


@dataclasses.dataclass
class Graph:
    start: List[int] = dataclasses.field(default_factory=lambda: [1000, 1000])
    head: List[int] = dataclasses.field(default_factory=lambda: [1000, 1000])
    tail: List[int] = dataclasses.field(default_factory=lambda: [1000, 1000])
    knots: List[List[int]] = dataclasses.field(default_factory=lambda: [[1000, 1000] for _ in range(9)])
    game_map: List[List[int]] = dataclasses.field(
        default_factory=lambda: [[0 for _ in range(2000)] for _ in range(2000)]
    )
    gap: List[int] = dataclasses.field(default_factory=lambda: [0, 0])
    gaps: List[List[int]] = dataclasses.field(default_factory=lambda: [[0, 0] for _ in range(9)])
    visited = 1

    gaps_map = {
        (2, 0): 'D',
        (-2, 0): 'U',
        (0, 2): 'R',
        (0, -2): 'L',
        (2, 1): 'D',
        (-2, 1): 'U',
        (1, 2): 'R',
        (1, -2): 'L',
        (-1, 2): 'R',
        (-1, -2): 'L',
        (2, -1): 'D',
        (-2, -1): 'U',
        (2, 2): 'DR',
        (2, -2): 'DL',
        (-2, -2): 'UL',
        (-2, 2): 'UR',
    }

    moves_map = {
        'U': (-1, 0),
        'R': (0, 1),
        'D': (1, 0),
        'L': (0, -1),
        'DR': (1, 1),
        'DL': (1, -1),
        'UL': (-1, -1),
        'UR': (-1, 1),
    }

    mirror_moves_map = {
        'L': 'R',
        'U': 'D',
        'R': 'L',
        'D': 'U',
        'DR': 'UL',
        'DL': 'UR',
        'UL': 'DR',
        'UR': 'DL',
    }

    def sum_list(self, origin: List[int], gap: (int, int), is_increment: bool = True):
        if is_increment:
            new_list = [origin[0] + gap[0], origin[1] + gap[1]]
        else:
            new_list = [origin[0] - gap[0], origin[1] - gap[1]]
        return new_list

    def move(self, move: List):
        for _ in range(int(move[1])):
            self.move_head(move[0])
            if tuple(self.gap) in self.gaps_map:
                self.chase_tail(self.gaps_map[tuple(self.gap)])

    def move_with_knots(self, move: List):
        for _ in range(int(move[1])):
            self.move_head(move[0])
            self.gaps[0] = self.gap
            for i in range(9):
                if tuple(self.gaps[i]) in self.gaps_map:
                    if i == 0:
                        prev_knot = self.head
                    else:
                        prev_knot = self.knots[i - 1]
                    self.chase_knot(i, prev_knot, self.gaps_map[tuple(self.gaps[i])])
            self.gap = self.gaps[0]

    def move_head(self, move: str):
        move_action = self.moves_map[move]
        self.head = self.sum_list(self.head, move_action)
        self.gap = self.sum_list(self.gap, move_action)

    def chase_tail(self, move: str):
        move_action = self.moves_map[self.mirror_moves_map[move]]
        self.tail = self.sum_list(self.head, move_action)
        self.gap = self.moves_map[move]
        if self.game_map[self.tail[0]][self.tail[1]] == 0:
            self.game_map[self.tail[0]][self.tail[1]] = 1
            self.visited += 1

    def chase_knot(self, index: int, prev_knot: List[int], move: str):
        move_action = self.moves_map[self.mirror_moves_map[move]]
        self.knots[index] = self.sum_list(prev_knot, move_action)
        self.gaps[index] = self.moves_map[move]
        if index == 8:
            if self.game_map[self.knots[index][0]][self.knots[index][1]] == 0:
                self.game_map[self.knots[index][0]][self.knots[index][1]] = 1
                self.visited += 1
        else:
            self.gaps[index + 1] = self.sum_list(self.knots[index], self.knots[index + 1], False)


def get_moves():
    moves = []
    with open(input_path) as f:
        for line in f:
            line = line.replace('\n', '')
            moves.append(line.split())
    return moves


def solution1(moves):
    graph = Graph()
    graph.game_map[graph.start[0]][graph.start[1]] = 1
    for move in moves:
        graph.move(move)
    return graph.visited


def solution2(moves):
    graph = Graph()
    graph.game_map[graph.start[0]][graph.start[1]] = 1
    for move in moves:
        graph.move_with_knots(move)
    return graph.visited


if __name__ == '__main__':
    moves = get_moves()
    print(solution1(moves))
    print(solution2(moves))
