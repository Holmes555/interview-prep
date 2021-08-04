class MyQueue1:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.que = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.que.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.que.pop(0)

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.que[0]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.que


class MyQueue2:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.s1.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        self.peek()
        return self.s2.pop(0)

    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not (self.s1 or self.s2)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
