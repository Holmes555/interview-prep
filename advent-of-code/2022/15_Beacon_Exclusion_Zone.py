import re

input_path = 'input/15_Beacon_Exclusion_Zone.txt'


def get_distance(point1, point2):
    return abs(point2[0] - point1[0]) + abs(point2[1] - point1[1])


def get_points():
    points = []
    min_x = 10**9
    max_x = -(10**9)
    min_y = 10**9
    max_y = -(10**9)
    with open(input_path) as f:
        for line in f:
            line = line.replace('\n', '')
            point = [int(s) for s in re.findall(r'-?\d+\.?\d*', line)]
            if point[0] < min_x:
                min_x = point[0]
            if point[2] < min_x:
                min_x = point[2]
            if point[0] > max_x:
                max_x = point[0]
            if point[2] > max_x:
                max_x = point[2]
            if point[1] < min_y:
                min_y = point[1]
            if point[3] < min_y:
                min_y = point[3]
            if point[1] > max_y:
                max_y = point[1]
            if point[3] > max_y:
                max_y = point[3]
            points.append((point[:2], point[2:], get_distance(point[:2], point[2:])))
    return points, min_x, max_x, max_y, min_y


def fill_map(beacon_map, point):
    try:
        if point[0] < 0 or point[1] < 0:
            raise IndexError
        if beacon_map[point[0]][point[1]] == '.':
            beacon_map[point[0]][point[1]] = '#'
    except IndexError:
        pass
    return beacon_map


def build_map(points, min_x, max_x, max_y, min_y, extension=0):
    beacon_map = [['.' for _ in range(max_x - min_x + 1 + extension)] for _ in range(max_y - min_y + 1)]
    row = 10 - min_y
    for point in points:
        signal = point[0]
        beacon_map[signal[1] - min_y][signal[0] - min_x + int(extension / 2)] = 'S'
        beacon_map[point[1][1] - min_y][point[1][0] - min_x + int(extension / 2)] = 'B'
        for i in range(point[2] + 1):
            for j in range(0, point[2] - i + 1):
                beacon_map = fill_map(beacon_map, (signal[1] - min_y - i, signal[0] - min_x + int(extension / 2) - j))
                beacon_map = fill_map(beacon_map, (signal[1] - min_y - i, signal[0] - min_x + int(extension / 2) + j))
                beacon_map = fill_map(beacon_map, (signal[1] - min_y + i, signal[0] - min_x + int(extension / 2) - j))
                beacon_map = fill_map(beacon_map, (signal[1] - min_y + i, signal[0] - min_x + int(extension / 2) + j))
    return beacon_map, row


def build_map2(points, max_p=4000001):
    # beacon_map = [['.' for _ in range(max_p)] for _ in range(max_p)]
    # [print(l) for l in beacon_map]
    for i in range(max_p):
        row_b = []
        for point in points:
            signal = point[0]
            line_len = point[2] * 2 + 1 - abs(signal[1] - i - 1)
            if line_len <= 0:
                continue
            left = signal[0] - point[2] - abs(signal[1] - i - 1)
            right = signal[0] + point[2] - abs(signal[1] - i - 1)
            start = left if left > 0 else 0
            if right < 0:
                finish = 0
            elif right > max_p:
                finish = max_p
            else:
                finish = right
            if start == finish:
                continue
            # start = signal[0] - point[2] - abs(signal[1] - i - 1) if signal[0] - point[2] > 0 else 0
            # finish = signal[0] + point[2] - abs(signal[1] - i - 1) if signal[0] + point[2] < max_p - 1 else max_p - 1
            # row_b[start:finish] = '#'*line_len
            # not_free = '#'*line_len
            row_b = ['#' if start <= i <= finish else row_b[i] for i in range(max_p)]
            # print(row_b)
        try:
            x = row_b.index('.')
            return x * (max_p - 1) + i + 1
        except ValueError:
            pass


def build_row(points, min_x, max_x, row=2000000, extension=0):
    counter = 0
    for x in range(min_x - int(extension / 2), max_x + 1 + int(extension / 2)):
        for point in points:
            if point[1][0] != x:
                break
            if get_distance((x, row), point[0]) <= point[2]:
                counter += 1
                break
    return counter


def slow_search(points, max_p=4000001):
    free_point = False
    for y in range(max_p):
        for x in range(max_p):
            for point in points:
                if point[1] != (x, y):
                    break
                if get_distance((x, y), point[0]) <= point[2]:
                    free_point = True
                    break
            if free_point:
                return x * (max_p - 1) + y


def solution1(points, min_x, max_x):
    return build_row(points, min_x, max_x, 2000000, 10**5)


def solution2(points, max_p=4000001):
    return build_map2(points)


if __name__ == '__main__':
    points, min_x, max_x, max_y, min_y = get_points()
    print(points, min_x, max_x, max_y, min_y)
    # beacon_map, row = build_map(points, min_x, max_x, max_y, min_y)
    # [print(l) for l in beacon_map]
    # print(solution1(points, min_x, max_x))
    print(solution2(points))

# 16_Proboscidea_Volcanium

# import re
#
# input_path = 'input/15_Beacon_Exclusion_Zone.txt'
#
#
# def get_distance(point1, point2):
#     return abs(point2[0] - point1[0]) + abs(point2[1] - point1[1])
#
#
# def get_points():
#     points = []
#     min_x = 10**9
#     max_x = -10**9
#     min_y = 10**9
#     max_y = -10**9
#     with open(input_path) as f:
#         for line in f:
#             line = line.replace('\n', '')
#             point = [int(s) for s in re.findall(r'-?\d+\.?\d*', line)]
#             if point[0] < min_x:
#                 min_x = point[0]
#             if point[2] < min_x:
#                 min_x = point[2]
#             if point[0] > max_x:
#                 max_x = point[0]
#             if point[2] > max_x:
#                 max_x = point[2]
#             if point[1] < min_y:
#                 min_y = point[1]
#             if point[3] < min_y:
#                 min_y = point[3]
#             if point[1] > max_y:
#                 max_y = point[1]
#             if point[3] > max_y:
#                 max_y = point[3]
#             points.append((point[:2], point[2:], get_distance(point[:2], point[2:])))
#     return points, min_x, max_x, max_y, min_y
#
#
# def fill_map(beacon_map, point):
#     try:
#         if point[0] < 0 or point[1] < 0:
#             raise IndexError
#         if beacon_map[point[0]][point[1]] == '.':
#             beacon_map[point[0]][point[1]] = '#'
#     except IndexError:
#         pass
#     return beacon_map
#
#
# def build_map(points, min_x, max_x, max_y, min_y, extension=0):
#     beacon_map = [['.' for _ in range(max_x - min_x + 1 + extension)] for _ in range(max_y - min_y + 1)]
#     row = 2000000 - min_y
#     for point in points:
#         signal = point[0]
#         beacon_map[signal[1] - min_y][signal[0] - min_x + int(extension / 2)] = 'S'
#         beacon_map[point[1][1] - min_y][point[1][0] - min_x + int(extension / 2)] = 'B'
#         for i in range(point[2] + 1):
#             for j in range(0, point[2] - i + 1):
#                 beacon_map = fill_map(beacon_map, (signal[1] - min_y - i, signal[0] - min_x + int(extension / 2) - j))
#                 beacon_map = fill_map(beacon_map, (signal[1] - min_y - i, signal[0] - min_x + int(extension / 2) + j))
#                 beacon_map = fill_map(beacon_map, (signal[1] - min_y + i, signal[0] - min_x + int(extension / 2) - j))
#                 beacon_map = fill_map(beacon_map, (signal[1] - min_y + i, signal[0] - min_x + int(extension / 2) + j))
#     return beacon_map, row
#
#
# def build_row(points, min_x, max_x, max_y, min_y, extension=0):
#     row = 2000000
#     counter = 0
#     for x in range(min_x - int(extension / 2), max_x + 1 + int(extension / 2)):
#         for point in points:
#             if point[1] != (x, row):
#                 if get_distance((x, row), point[0]) <= point[2]:
#                     counter += 1
#                     break
#     return counter
#
#
# def solution1(beacon_map, row):
#     # [print(l) for l in beacon_map]
#     counter = 0
#     # print(beacon_map[10])
#     for p in beacon_map[row]:
#         if p in {'#'}:
#             counter += 1
#     return counter
#
#
#
# def solution2(sand_map, sand_start):
#     counter = 0
#     while True:
#         can_move = True
#         next_point = sand_start
#         next_point = pouring_sand(sand_map, next_point, can_move)
#         counter += 1
#         if next_point == sand_start:
#             break
#     return counter
#
#
# if __name__ == '__main__':
#     points, min_x, max_x, max_y, min_y = get_points()
#     print(points, min_x, max_x, max_y, min_y)
#     print(build_row(points, min_x, max_x, max_y, min_y, 10**7))
#     # beacon_map, row = build_map(points, min_x, max_x, max_y, min_y, 2000000)
#     # print(solution1(beacon_map, row))
#     # print(solution2(sand_map2, sand_start))

# 17_Pyroclastic_Flow

# import re
#
# input_path = 'input/17_Pyroclastic_Flow.txt'
#
#
# def get_distance(point1, point2):
#     return abs(point2[0] - point1[0]) + abs(point2[1] - point1[1])
#
#
# def get_points():
#     points = []
#     min_x = 10**9
#     max_x = -10**9
#     min_y = 10**9
#     max_y = -10**9
#     with open(input_path) as f:
#         for line in f:
#             line = line.replace('\n', '')
#             point = [int(s) for s in re.findall(r'-?\d+\.?\d*', line)]
#             if point[0] < min_x:
#                 min_x = point[0]
#             if point[2] < min_x:
#                 min_x = point[2]
#             if point[0] > max_x:
#                 max_x = point[0]
#             if point[2] > max_x:
#                 max_x = point[2]
#             if point[1] < min_y:
#                 min_y = point[1]
#             if point[3] < min_y:
#                 min_y = point[3]
#             if point[1] > max_y:
#                 max_y = point[1]
#             if point[3] > max_y:
#                 max_y = point[3]
#             points.append((point[:2], point[2:], get_distance(point[:2], point[2:])))
#     return points, min_x, max_x, max_y, min_y
#
#
# def fill_map(beacon_map, point):
#     try:
#         if point[0] < 0 or point[1] < 0:
#             raise IndexError
#         if beacon_map[point[0]][point[1]] == '.':
#             beacon_map[point[0]][point[1]] = '#'
#     except IndexError:
#         pass
#     return beacon_map
#
#
# def build_map(points, min_x, max_x, max_y, min_y, extension=0):
#     beacon_map = [['.' for _ in range(max_x - min_x + 1 + extension)] for _ in range(max_y - min_y + 1)]
#     row = 2000000 - min_y
#     for point in points:
#         signal = point[0]
#         beacon_map[signal[1] - min_y][signal[0] - min_x + int(extension / 2)] = 'S'
#         beacon_map[point[1][1] - min_y][point[1][0] - min_x + int(extension / 2)] = 'B'
#         for i in range(point[2] + 1):
#             for j in range(0, point[2] - i + 1):
#                 beacon_map = fill_map(beacon_map, (signal[1] - min_y - i, signal[0] - min_x + int(extension / 2) - j))
#                 beacon_map = fill_map(beacon_map, (signal[1] - min_y - i, signal[0] - min_x + int(extension / 2) + j))
#                 beacon_map = fill_map(beacon_map, (signal[1] - min_y + i, signal[0] - min_x + int(extension / 2) - j))
#                 beacon_map = fill_map(beacon_map, (signal[1] - min_y + i, signal[0] - min_x + int(extension / 2) + j))
#     return beacon_map, row
#
#
# def build_row(points, min_x, max_x, row=2000000, extension=0):
#     counter = 0
#     for x in range(min_x - int(extension / 2), max_x + 1 + int(extension / 2)):
#         for point in points:
#             if point[1][0] != x:
#                 break
#             if get_distance((x, row), point[0]) <= point[2]:
#                 counter += 1
#                 break
#     return counter
#
#
# def solution1(points, min_x, max_x):
#     return build_row(points, min_x, max_x, 2000000, 10**5)
#
#
# def solution2(points, max_p=4000001):
#     free_point = False
#     for y in range(max_p):
#         for x in range(max_p):
#             for point in points:
#                 if point[1][0] != x:
#                     break
#                 if get_distance((x, y), point[0]) <= point[2]:
#                     free_point = True
#                     break
#             if free_point:
#                 return x * (max_p - 1) + y
#
#
# if __name__ == '__main__':
#     points, min_x, max_x, max_y, min_y = get_points()
#     print(points, min_x, max_x, max_y, min_y)
#     # beacon_map, row = build_map(points, min_x, max_x, max_y, min_y, 2000000)
#     # print(solution1(points, min_x, max_x))
#     print(solution2(points))
