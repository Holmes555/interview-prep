import re

input_path = 'input/1_Trebuchet.txt'


def solution1():
    calibr = 0
    with open(input_path) as f:
        for line in f:
            first_n = None
            last_n = None
            for c in line:
                if first_n is None:
                    if c.isdigit():
                        first_n = int(c)
                elif c.isdigit():
                    last_n = int(c)
            if last_n is None:
                last_n = first_n
            calibr += first_n * 10 + last_n
    return calibr


def solution2():
    calibr = 0
    digits = [
        '1',
        '2',
        '3',
        '4',
        '5',
        '6',
        '7',
        '8',
        '9',
        'one',
        'two',
        'three',
        'four',
        'five',
        'six',
        'seven',
        'eight',
        'nine',
    ]
    str_to_digits = {
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
    }
    with open(input_path) as f:
        for line in f:
            indexes = {}

            for d in digits:
                inds = [m.start() for m in re.finditer(d, line)]
                for i in inds:
                    indexes[i] = d

            min_i = min(indexes.keys())
            max_i = max(indexes.keys())
            first_n = str_to_digits[indexes[min_i]]
            last_n = str_to_digits[indexes[max_i]]
            calibr += first_n * 10 + last_n
    return calibr


if __name__ == '__main__':
    print(solution1())
    print(solution2())
