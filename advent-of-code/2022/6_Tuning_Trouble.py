input_path = 'input/6_Tuning_Trouble.txt'


def get_distinct(n: int):
    marker_set = set()
    marker_dict = {}
    marker_list = []
    with open(input_path) as f:
        line = f.readline()
        for i, c in enumerate(line):
            if c not in marker_dict:
                marker_dict[c] = 0
            marker_dict[c] += 1
            marker_set.add(c)
            marker_list.append(c)
            if len(marker_set) == n:
                return i + 1
            if len(marker_list) == n:
                c_out = marker_list.pop(0)
                marker_dict[c_out] -= 1
                if marker_dict[c_out] == 0:
                    marker_set.remove(c_out)


def solution1():
    return get_distinct(4)


def solution2():
    return get_distinct(14)


if __name__ == '__main__':
    print(solution1())
    print(solution2())
