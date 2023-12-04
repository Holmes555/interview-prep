from functools import reduce

input_path = 'input/3_Gear_Ratios.txt'


MOVES = {
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1),
    (1, 1),
    (1, -1),
    (-1, -1),
    (-1, 1),
}


def check_move(move, size):
    return 0 <= move[0] <= size[0] and 0 <= move[1] <= size[1]


def read_map():
    gears_map = {}
    symbols_map = []
    with open(input_path) as f:
        for i, line in enumerate(f):
            start_j = -1
            for j, c in enumerate(line):
                if c.isdigit():
                    if start_j == -1:
                        start_j = j
                else:
                    if start_j != -1:
                        gear = int(line[start_j:j])
                        all_indexes = {(i, k) for k in range(start_j, j)}
                        for k in range(start_j, j):
                            gears_map[(i, k)] = (gear, all_indexes)
                        start_j = -1
                    if c not in '. \n':
                        symbols_map.append((i, j))
        size = [i, j]
    return gears_map, symbols_map, size


def get_gears(symbol, size, gears_map):
    forbidden_moves = set()
    gears = []
    for m in MOVES:
        move = (symbol[0] + m[0], symbol[1] + m[1])
        if check_move(move, size) and move not in forbidden_moves:
            if move in gears_map:
                gear, all_indexes = gears_map[move]
                forbidden_moves.update(all_indexes)
                gears.append(gear)
    return gears


def solution1():
    gears = []
    gears_map, symbols_map, size = read_map()

    for symbol in symbols_map:
        gears.extend(get_gears(symbol, size, gears_map))
    return sum(gears)


def solution2():
    gears = []
    gears_map, symbols_map, size = read_map()

    for symbol in symbols_map:
        potential = get_gears(symbol, size, gears_map)
        if len(potential) > 1:
            gears.append(reduce((lambda x, y: x * y), potential))
    return sum(gears)


if __name__ == '__main__':
    print(solution1())
    print(solution2())
