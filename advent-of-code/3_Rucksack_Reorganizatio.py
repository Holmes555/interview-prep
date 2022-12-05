import string

input_path = 'input/3_Rucksack_Reorganizatio.txt'


def solution1():
    map1 = {v: i + 1 for i, v in enumerate(string.ascii_lowercase + string.ascii_uppercase)}
    result = 0
    with open(input_path) as f:
        for line in f:
            mid = int(len(line[:-1]) / 2)
            part1 = line[:mid]
            part2 = line[mid:]
            for c in part1:
                if c in part2:
                    result += map1[c]
                    break
    return result


def solution2():
    map1 = {v: i + 1 for i, v in enumerate(string.ascii_lowercase + string.ascii_uppercase)}
    result = 0
    group = []
    with open(input_path) as f:
        for line in f:
            group.append(line)
            if len(group) == 3:
                for c in group[0]:
                    if c in group[1] and c in group[2]:
                        result += map1[c]
                        group = []
                        break
    return result


if __name__ == '__main__':
    print(solution1())
    print(solution2())
