import math
import re

input_path = 'input/8_Haunted_Wasteland.txt'


MOVE_TO_INDEX = {'L': 0, 'R': 1}


def get_moves():
    map = {}
    start_s = []
    with open(input_path) as f:
        moves = f.readline()[:-1]
        f.readline()
        for line in f:
            parts = re.findall('[A-Z]+', line)
            map[parts[0]] = (parts[1], parts[2])
            if parts[0][-1] == 'A':
                start_s.append(parts[0])
    return moves, map, start_s


def solution1():
    moves, map, _ = get_moves()
    cur_s = 'AAA'
    final_s = 'ZZZ'
    i = 0
    len_m = len(moves)
    while True:
        m = moves[i % len_m]
        j = MOVE_TO_INDEX[m]
        cur_s = map[cur_s][j]
        i += 1
        if cur_s == final_s:
            break
    return i


def solution2():
    moves, map, start_s = get_moves()
    i = 0
    len_m = len(moves)
    len_s = len(start_s)
    final_it = [0] * len_s
    while True:
        for k in range(len_s):
            m = moves[i % len_m]
            j = MOVE_TO_INDEX[m]
            cur_s = start_s.pop(0)
            cur_s = map[cur_s][j]
            start_s.append(cur_s)
            if cur_s[-1] == 'Z':
                final_it[k] = i + 1
        i += 1
        if all(final_it) != 0:
            break
    return math.lcm(*final_it)


if __name__ == '__main__':
    print(solution1())
    print(solution2())
