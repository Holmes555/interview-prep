class MyCircularQueue:
    def __init__(self, k: int):
        self.length = 0
        self.head = -1
        self.tail = -1
        self.size = k
        self.q = [None] * self.size

    def enQueue(self, value: int) -> bool:
        if self.length < self.size:
            if self.head == -1:
                self.head = 0
            self.tail = (self.tail + 1) % self.size
            self.q[self.tail] = value
            self.length += 1
            return True
        return False

    def deQueue(self) -> bool:
        if self.length > 0:
            self.q[self.head] = None
            self.head = (self.head + 1) % self.size
            self.length -= 1
            return True
        return False

    def Front(self) -> int:
        return self.q[self.head] if self.length > 0 and self.head != -1 else -1

    def Rear(self) -> int:
        return self.q[self.tail] if self.length > 0 and self.tail != -1 else -1

    def isEmpty(self) -> bool:
        return self.length == 0

    def isFull(self) -> bool:
        return self.length == self.size


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
