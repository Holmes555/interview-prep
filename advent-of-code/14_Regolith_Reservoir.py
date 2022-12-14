input_path = 'input/14_Regolith_Reservoir.txt'


def get_rocks():
    rocks = []
    min_x = 1000
    max_x = 0
    max_y = 0
    with open(input_path) as f:
        for line in f:
            if line != '\n':
                line = line.replace('\n', '')
                points = []
                for point in line.split(' -> '):
                    x, y = point.split(',')
                    x = int(x)
                    y = int(y)
                    if x < min_x:
                        min_x = x
                    if x > max_x:
                        max_x = x
                    if y > max_y:
                        max_y = y
                    points.append((x, y))
                rocks.append(points)
    return rocks, min_x, max_x, max_y


def build_map(rocks, min_x, max_x, max_y, extension=0):
    sand_map = [['.' for _ in range(max_x - min_x + 1 + extension)] for _ in range(max_y + 1)]
    sand_start = (500 - min_x + int(extension / 2), 0)
    sand_map[sand_start[1]][sand_start[0]] = '+'
    for points in rocks:
        prev_x = None
        prev_y = None
        for x, y in points:
            sand_map[y][x - min_x + int(extension / 2)] = '#'
            if prev_x is not None and prev_y is not None:
                if x > prev_x:
                    for i in range(prev_x - min_x + int(extension / 2), x - min_x + int(extension / 2)):
                        sand_map[y][i] = '#'
                if x < prev_x:
                    for i in range(x - min_x + int(extension / 2), prev_x - min_x + int(extension / 2)):
                        sand_map[y][i] = '#'
                if y > prev_y:
                    for i in range(prev_y, y):
                        sand_map[i][x - min_x + int(extension / 2)] = '#'
                if y < prev_y:
                    for i in range(y, prev_y):
                        sand_map[i][x - min_x + int(extension / 2)] = '#'
            prev_x, prev_y = x, y
    return sand_map, sand_start


sand_moves = [
    (0, 1),
    (-1, 1),
    (1, 1),
]


def pouring_sand(sand_map, next_point, can_move):
    while can_move:
        stopped = True
        for move in sand_moves:
            mb_next_point = (next_point[0] + move[0], next_point[1] + move[1])
            if sand_map[mb_next_point[1]][mb_next_point[0]] == '.':
                next_point = mb_next_point
                stopped = False
                break
        if stopped:
            sand_map[next_point[1]][next_point[0]] = 'o'
            can_move = False
    return next_point


def solution1(sand_map, sand_start):
    counter = 0
    while True:
        can_move = True
        next_point = sand_start
        try:
            pouring_sand(sand_map, next_point, can_move)
            counter += 1
        except IndexError:
            return counter


def solution2(sand_map, sand_start):
    counter = 0
    while True:
        can_move = True
        next_point = sand_start
        next_point = pouring_sand(sand_map, next_point, can_move)
        counter += 1
        if next_point == sand_start:
            break
    return counter


if __name__ == '__main__':
    rocks, min_x, max_x, max_y = get_rocks()
    sand_map1, sand_start = build_map(rocks, min_x, max_x, max_y)
    print(solution1(sand_map1, sand_start))
    sand_map2, sand_start = build_map(rocks, min_x, max_x, max_y, 2000)
    width = len(sand_map2[0])
    sand_map2.append(['.' for _ in range(width)])
    sand_map2.append(['#' for _ in range(width)])
    print(solution2(sand_map2, sand_start))
