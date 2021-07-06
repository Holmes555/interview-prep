import operator
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv,
        }
        for token in tokens:
            if token not in ops:
                stack.append(int(token))
            else:
                operand2 = stack.pop()
                operand1 = stack.pop()
                operand2 = int(ops[token](operand1, operand2))
                stack.append(operand2)

        return stack.pop()
