import math

input_path = 'input/10_Cathode-Ray_Tube.txt'


def get_signals():
    signals = []
    with open(input_path) as f:
        for line in f:
            line = line.replace('\n', '')
            signals.append(line)
    return signals


signal_milestones = {20, 60, 100, 140, 180, 220}


def calc_signal(result, vx: int, cycles: int):
    if cycles in signal_milestones:
        result += vx * cycles
    return result


def draw_image(result, vx: int, cycles: int):
    row = math.floor((cycles - 1) / 40)
    index = cycles - 40 * row - 1
    result[row][index] = '#' if vx <= index <= vx + 2 else '.'
    return result


def noop(signal: str, result, value: int, cycles: int, func):
    cycles += 1
    result = func(result, value, cycles)
    return result, value, cycles


def addx(signal: str, result, value: int, cycles: int, func):
    vx = int(signal.split('addx')[1])
    cycles += 1
    result = func(result, value, cycles)
    cycles += 1
    result = func(result, value, cycles)
    return result, value + vx, cycles


signal_map = {
    'noop': noop,
    'addx': addx,
}


def solution1(signals):
    result = 0
    cycles = 0
    value = 1
    for signal in signals:
        for command, func in signal_map.items():
            if signal.startswith(command):
                result, value, cycles = func(signal, result, value, cycles, calc_signal)
    return result


def solution2(signals):
    cycles = 0
    value = 0
    image = [['.' for _ in range(40)] for _ in range(6)]
    for signal in signals:
        for command, func in signal_map.items():
            if signal.startswith(command):
                result, value, cycles = func(signal, image, value, cycles, draw_image)
    return image


if __name__ == '__main__':
    signals = get_signals()
    print(solution1(signals))
    [print(' '.join(line)) for line in solution2(signals)]


"""
# # # . . # . . # . . # # . . # # # # . . # # . . . . # # . # # # . . # # # . .
# . . # . # . # . . # . . # . . . . # . # . . # . . . . # . # . . # . # . . # .
# . . # . # # . . . # . . # . . . # . . # . . # . . . . # . # # # . . # . . # .
# # # . . # . # . . # # # # . . # . . . # # # # . . . . # . # . . # . # # # . .
# . # . . # . # . . # . . # . # . . . . # . . # . # . . # . # . . # . # . # . .
# . . # . # . . # . # . . # . # # # # . # . . # . . # # . . # # # . . # . . # .
"""
