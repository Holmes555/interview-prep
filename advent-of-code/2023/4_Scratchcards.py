input_path = 'input/4_Scratchcards.txt'


def get_cur_game(line):
    parts = line.split(': ')
    numbers = parts[1].split('| ')
    winning = set(numbers[0].split())
    yours = set(numbers[1].split())
    return winning, yours


def solution1():
    score = 0
    with open(input_path) as f:
        for i, line in enumerate(f):
            winning, yours = get_cur_game(line)
            pow_2 = -1
            for v in yours:
                if v in winning:
                    pow_2 += 1
            if pow_2 >= 0:
                score += pow(2, pow_2)
    return score


def solution2():
    score = [0] * 218
    with open(input_path) as f:
        for i, line in enumerate(f):
            winning, yours = get_cur_game(line)
            number = 0
            for v in yours:
                if v in winning:
                    number += 1
            score[i] += 1
            for j in range(i + 1, i + number + 1):
                score[j] += score[i]
    return sum(score)


if __name__ == '__main__':
    print(solution1())
    print(solution2())
