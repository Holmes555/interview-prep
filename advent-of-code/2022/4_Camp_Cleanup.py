input_path = 'input/4_Camp_Cleanup.txt'


def solution1():
    result = 0
    with open(input_path) as f:
        for line in f:
            line = line.replace('\n', '')
            group1, group2 = line[:].split(',')
            ge11, ge12 = group1[:].split('-')
            ge21, ge22 = group2[:].split('-')
            if (int(ge11) <= int(ge21) and int(ge12) >= int(ge22)) or (
                int(ge11) >= int(ge21) and int(ge12) <= int(ge22)
            ):
                result += 1
    return result


def solution2():
    result = 0
    with open(input_path) as f:
        for line in f:
            line = line.replace('\n', '')
            group1, group2 = line[:].split(',')
            ge11, ge12 = group1[:].split('-')
            ge21, ge22 = group2[:].split('-')
            if not (int(ge12) < int(ge21) or int(ge11) > int(ge22)):
                result += 1
    return result


if __name__ == '__main__':
    print(solution1())
    print(solution2())
