input_path = 'input/2_Cube_Conundrum.txt'


CUBES = {'red': 12, 'green': 13, 'blue': 14}


def get_cur_cubes(line):
    cur_cubes = {'red': 0, 'green': 0, 'blue': 0}
    parts = line.split(': ')
    tries = parts[1].split('; ')
    for t in tries:
        cubes_try = t.split(', ')
        for c in cubes_try:
            res = c.split()
            if int(res[0]) > cur_cubes[res[1]]:
                cur_cubes[res[1]] = int(res[0])
    return cur_cubes


def solution1():
    games = []
    with open(input_path) as f:
        for i, line in enumerate(f):
            cur_cubes = get_cur_cubes(line)
            for k, v in CUBES.items():
                if cur_cubes[k] > v:
                    break
            else:
                games.append(i + 1)
    return sum(games)


def solution2():
    games = []
    with open(input_path) as f:
        for i, line in enumerate(f):
            cur_cubes = get_cur_cubes(line)
            games.append(1)
            for v in cur_cubes.values():
                games[i] *= v
    return sum(games)


if __name__ == '__main__':
    print(solution1())
    print(solution2())
