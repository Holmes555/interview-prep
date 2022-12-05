input_path = 'input/2_Rock_Paper_Scissors.txt'


def loop_front(index):
    index = index % 3
    return index + 1


def loop_back(index):
    if index == 1:
        index = 4
    return index - 1


def solution1():
    map1 = {'A': 1, 'B': 2, 'C': 3}
    map2 = {'X': 1, 'Y': 2, 'Z': 3}
    result = 0
    with open(input_path) as f:
        for line in f:
            abc, xyz = line.split(' ')
            xyz = xyz[:-1]
            result += map2[xyz]
            if map2[xyz] == map1[abc]:
                result += 3
            if (
                (map2[xyz] == 1 and map1[abc] == 3)
                or (map2[xyz] == 2 and map1[abc] == 1)
                or (map2[xyz] == 3 and map1[abc] == 2)
            ):
                result += 6
    return result


def solution2():
    map1 = {'A': 1, 'B': 2, 'C': 3}
    map2 = {'X': 0, 'Y': 3, 'Z': 6}
    result = 0
    with open(input_path) as f:
        for line in f:
            abc, xyz = line.split(' ')
            xyz = xyz[:-1]
            result += map2[xyz]
            if map2[xyz] == 0:
                result += loop_back(map1[abc])
            if map2[xyz] == 3:
                result += map1[abc]
            if map2[xyz] == 6:
                result += loop_front(map1[abc])
    return result


if __name__ == '__main__':
    print(solution1())
    print(solution2())
