class MyStack:

    def __init__(self):
        self._stack = []

    def push(self, x: int) -> None:
        self._stack.append(x)

    def pop(self) -> int:
        return self._stack.pop(-1)

    def top(self) -> int:
        return self._stack[-1]

    def empty(self) -> bool:
        return not bool(self._stack)


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()