input_path_1 = 'input/5_Supply_Stacks_1.txt'
input_path_2 = 'input/5_Supply_Stacks_2.txt'


def read_stacks():
    stacks = []
    input_stack = []
    with open(input_path_1) as f:
        for line in f:
            line = line.replace('\n', '')
            group = line[:].split(' ')
            input_stack.append(group)

    for i, group in enumerate(input_stack[::-1]):
        for j, el in enumerate(group):
            if el != '0':
                if len(stacks) <= j:
                    stacks.append([])
                stacks[j].append(el)
    return stacks


def solution1():
    stacks = read_stacks()

    with open(input_path_2) as f:
        for line in f:
            line = line.replace('\n', '')
            command = line[:].split(' ')
            for i in range(0, int(command[1])):
                v = stacks[int(command[3]) - 1].pop()
                stacks[int(command[5]) - 1].append(v)

    result = ''
    for s in stacks:
        result += s[-1][1]
    return result


def solution2():
    stacks = read_stacks()

    with open(input_path_2) as f:
        for line in f:
            line = line.replace('\n', '')
            command = line[:].split(' ')
            v = stacks[int(command[3]) - 1][-int(command[1]) :]
            stacks[int(command[3]) - 1] = stacks[int(command[3]) - 1][: -int(command[1])]
            stacks[int(command[5]) - 1].extend(v)

    result = ''
    for s in stacks:
        result += s[-1][1]
    return result


if __name__ == '__main__':
    print(solution1())
    print(solution2())
