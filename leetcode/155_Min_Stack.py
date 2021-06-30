class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_el = []
        self.size = 0

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_el:
            self.min_el.append(min(self.min_el[self.size - 1], val))
        else:
            self.min_el.append(val)
        self.size += 1

    def pop(self) -> None:
        self.size -= 1
        self.min_el.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[self.size - 1]

    def getMin(self) -> int:
        return self.min_el[self.size - 1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
