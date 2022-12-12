import dataclasses
import math
from typing import Callable, List

input_path = 'input/11_Monkey_in_the_Middle.txt'


@dataclasses.dataclass
class Monkey:
    items: List[float]
    operation: Callable
    test: Callable
    count: int = 0

    bored_division: int = 3

    def bored(self, item: int):
        if self.bored_division == 0:
            return item
        return math.floor(item / self.bored_division)


def inspect(monkeys: List[Monkey]):
    for monkey in monkeys:
        while monkey.items:
            item = monkey.items.pop(0)
            item %= 9699690
            value = monkey.operation(item)
            value = monkey.bored(value)
            index = monkey.test(value)
            monkeys[index].items.append(value)
            monkey.count += 1


def solution1():
    monkeys = [
        Monkey(items=[54, 89, 94], operation=lambda x: x * 7, test=lambda x: 5 if x % 17 == 0 else 3),
        Monkey(items=[66, 71], operation=lambda x: x + 4, test=lambda x: 0 if x % 3 == 0 else 3),
        Monkey(items=[76, 55, 80, 55, 55, 96, 78], operation=lambda x: x + 2, test=lambda x: 7 if x % 5 == 0 else 4),
        Monkey(
            items=[93, 69, 76, 66, 89, 54, 59, 94], operation=lambda x: x + 7, test=lambda x: 5 if x % 7 == 0 else 2
        ),
        Monkey(items=[80, 54, 58, 75, 99], operation=lambda x: x * 17, test=lambda x: 1 if x % 11 == 0 else 6),
        Monkey(items=[69, 70, 85, 83], operation=lambda x: x + 8, test=lambda x: 2 if x % 19 == 0 else 7),
        Monkey(items=[89], operation=lambda x: x + 6, test=lambda x: 0 if x % 2 == 0 else 1),
        Monkey(items=[62, 80, 58, 57, 93, 56], operation=lambda x: x * x, test=lambda x: 6 if x % 13 == 0 else 4),
    ]
    # monkeys = [
    #     Monkey(items=[79, 98], operation=lambda x: x * 19, test=lambda x: 2 if x % 23 == 0 else 3),
    #     Monkey(items=[54, 65, 75, 74], operation=lambda x: x + 6, test=lambda x: 2 if x % 19 == 0 else 0),
    #     Monkey(items=[79, 60, 97], operation=lambda x: x * x, test=lambda x: 1 if x % 13 == 0 else 3),
    #     Monkey(items=[74], operation=lambda x: x + 3, test=lambda x: 0 if x % 17 == 0 else 1),
    # ]
    for _ in range(20):
        inspect(monkeys)
    monkeys.sort(key=lambda x: x.count, reverse=True)
    return monkeys[0].count * monkeys[1].count


def solution2():
    monkeys = [
        Monkey(items=[54, 89, 94], operation=lambda x: x * 7, test=lambda x: 5 if x % 17 == 0 else 3, bored_division=0),
        Monkey(items=[66, 71], operation=lambda x: x + 4, test=lambda x: 0 if x % 3 == 0 else 3, bored_division=0),
        Monkey(
            items=[76, 55, 80, 55, 55, 96, 78],
            operation=lambda x: x + 2,
            test=lambda x: 7 if x % 5 == 0 else 4,
            bored_division=0,
        ),
        Monkey(
            items=[93, 69, 76, 66, 89, 54, 59, 94],
            operation=lambda x: x + 7,
            test=lambda x: 5 if x % 7 == 0 else 2,
            bored_division=0,
        ),
        Monkey(
            items=[80, 54, 58, 75, 99],
            operation=lambda x: x * 17,
            test=lambda x: 1 if x % 11 == 0 else 6,
            bored_division=0,
        ),
        Monkey(
            items=[69, 70, 85, 83], operation=lambda x: x + 8, test=lambda x: 2 if x % 19 == 0 else 7, bored_division=0
        ),
        Monkey(items=[89], operation=lambda x: x + 6, test=lambda x: 0 if x % 2 == 0 else 1, bored_division=0),
        Monkey(
            items=[62, 80, 58, 57, 93, 56],
            operation=lambda x: x * x,
            test=lambda x: 6 if x % 13 == 0 else 4,
            bored_division=0,
        ),
    ]
    for _ in range(10000):
        inspect(monkeys)
    monkeys.sort(key=lambda x: x.count, reverse=True)
    return monkeys[0].count * monkeys[1].count


if __name__ == '__main__':
    print(solution1())
    print(solution2())
