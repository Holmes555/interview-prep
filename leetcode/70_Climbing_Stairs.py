class Solution:
    f = [0] * 50
    f[0] = f[1] = 1

    def fib_r(self, n):
        if n == 0 or n == 1:
            return 1
        self.f[n] = self.fib(n - 1) + self.fib(n - 2)
        return self.f[n]

    def fib(self, n):
        if n == 0 or n == 1:
            return 1
        for i in range(2, n + 1):
            self.f[i] = self.f[i - 1] + self.f[i - 2]
        return self.f[n]

    def climbStairs(self, n: int) -> int:
        return self.fib(n)
