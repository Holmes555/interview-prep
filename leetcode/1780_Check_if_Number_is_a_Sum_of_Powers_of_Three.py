import math


class Solution:
    def __init__(self):
        self.powers = set()

    def checkPowersOfThree(self, n: int) -> bool:
        power = math.log(n, 3)
        if power in self.powers:
            return False
        if 3 ** round(power) == n:
            return True
        power = math.floor(power)
        if power <= 0 or power in self.powers:
            return False
        self.powers.add(power)
        return self.checkPowersOfThree(n - 3**power)
