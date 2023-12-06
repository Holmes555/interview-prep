from functools import reduce

input_path = 'input/6_Wait_For_It.txt'


def get_stats():
    with open(input_path) as f:
        parts = f.readline().split(':')
        time = parts[1].split()
        parts = f.readline().split(':')
        distance = parts[1].split()
    return time, distance


def solution1():
    time, distance = get_stats()
    stats = {int(t): int(d) for t, d in zip(time, distance)}
    score = []
    for t, d in stats.items():
        optimal_t = int(t / 2)
        res = set()
        i = 0
        while i < optimal_t:
            if (t - optimal_t - i) * (optimal_t + i) > d:
                res.add(optimal_t + i)
            if (t - optimal_t + i) * (optimal_t - i) > d:
                res.add(optimal_t - i)
            i += 1
        score.append(len(res))
    return reduce((lambda x, y: x * y), score)


def solution2():
    time, distance = get_stats()
    time = ''.join(time)
    distance = ''.join(distance)
    stats = {int(time): int(distance)}
    score = []
    for t, d in stats.items():
        optimal_t = int(t / 2)
        res = set()
        i = 0
        while i < optimal_t:
            if (t - optimal_t - i) * (optimal_t + i) > d:
                res.add(optimal_t + i)
            if (t - optimal_t + i) * (optimal_t - i) > d:
                res.add(optimal_t - i)
            i += 1
        score.append(len(res))
    return reduce((lambda x, y: x * y), score)


if __name__ == '__main__':
    print(solution1())
    print(solution2())
