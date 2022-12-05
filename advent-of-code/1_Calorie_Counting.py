input_path = 'input/1_Calorie_Counting.txt'


def solution1():
    elves = []
    food = 0
    with open(input_path) as f:
        for line in f:
            if line != '\n':
                food += int(line)
            else:
                elves.append(food)
                food = 0
    return max(elves)


def solution2():
    elves = []
    food = 0
    with open(input_path) as f:
        for line in f:
            if line != '\n':
                food += int(line)
            else:
                elves.append(food)
                food = 0
    elves.sort()
    return sum(elves[:-4:-1])


if __name__ == '__main__':
    print(solution1())
    print(solution2())
