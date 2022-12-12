from typing import List, Set

input_path = 'input/12_Hill_Climbing_Algorithm.txt'


def get_hills_map():
    hills_map = []
    with open(input_path) as f:
        for line in f:
            line = line.replace('\n', '')
            hills_map.append(list(line))
    return hills_map


moves = [
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1),
]


def up(x, y):
    return ord(x) - ord(y) > 1


def down(x, y):
    return ord(y) - ord(x) > 1


def bfs_dijkstra(hills_map: List[List[str]], start_point: List, goal: (str, Set[str]), elev_calc):
    a = [start_point]
    visited = set()
    height = len(hills_map)
    width = len(hills_map[0])
    while a:
        node = a.pop(0)

        for m in moves:
            new_point = (node[2][0] + m[0], node[2][1] + m[1])
            if new_point[0] > height - 1 or new_point[0] < 0 or new_point[1] > width - 1 or new_point[1] < 0:
                continue
            value = hills_map[new_point[0]][new_point[1]]
            if value == goal[0] and node[0] in goal[1]:
                return node[3] + 1
            if new_point in visited or elev_calc(value, node[0]):
                continue
            visited.add(new_point)
            a.append((value, node[0], new_point, node[3] + 1))


def solution1(hills_map):
    return bfs_dijkstra(hills_map, ['a', 'a', (20, 0), 0], ('E', {'y', 'z'}), up)


def solution2(hills_map):
    return bfs_dijkstra(hills_map, ['z', 'z', (20, 148), 0], ('a', {'b', 'a'}), down)


if __name__ == '__main__':
    hills_map = get_hills_map()
    print(solution1(hills_map))
    print(solution2(hills_map))
