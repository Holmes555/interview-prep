import ast
import functools
from typing import List

input_path = 'input/13_Distress_Signal.txt'


def get_signals():
    signals = []
    with open(input_path) as f:
        for line in f:
            if line != '\n':
                line = line.replace('\n', '')
                signals.append(ast.literal_eval(line))
    return signals


def cmp(it1, it2):
    if isinstance(it1, int):
        if isinstance(it2, int):
            if it1 > it2:
                return False
            if it1 < it2:
                return True
            return None
        if isinstance(it2, list):
            return cmp([it1], it2)
    if isinstance(it1, list):
        if isinstance(it2, list):
            for i in range(len(it1)):
                if i >= len(it2):
                    return False
                r = cmp(it1[i], it2[i])
                if r is None:
                    continue
                return r
            if len(it1) == len(it2):
                return None
            return True
        if isinstance(it2, int):
            return cmp(it1, [it2])


def base_cmp(it1, it2):
    r = cmp(it1, it2)
    if r is None:
        return 0
    return 1 if r else -1


def compare(signals: List):
    result = 0
    for i, (item1, item2) in enumerate(signals):
        if cmp(item1, item2):
            result += i + 1
    return result


def sort(signals: List):
    signals.sort(key=functools.cmp_to_key(base_cmp), reverse=True)
    return (signals.index([[2]]) + 1) * (signals.index([[6]]) + 1)


def solution1(signals):
    return compare(signals)


def solution2(signals):
    return sort(signals)


if __name__ == '__main__':
    signals = get_signals()
    signals_1 = [(signals[i], signals[i + 1]) for i in range(0, len(signals) - 1, 2)]
    print(solution1(signals_1))
    signals_2 = signals + [[[2]], [[6]]]
    print(solution2(signals_2))
