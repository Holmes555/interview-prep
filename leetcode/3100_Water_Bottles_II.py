class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        total_drunk = numBottles
        empty_bottles = numBottles

        while empty_bottles >= numExchange:
            empty_bottles = empty_bottles - numExchange + 1
            total_drunk += 1
            numExchange += 1

        return total_drunk
