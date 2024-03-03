class MyStack:

    def __init__(self):
        self.lis = []

    def push(self, x: int) -> None:
        self.lis.append(x)

    def pop(self) -> int:
        temp = self.lis.pop()
        return temp

    def top(self) -> int:
        return self.lis[-1]

    def empty(self) -> bool:
        return len(self.lis)==0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()