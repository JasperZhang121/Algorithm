class MyQueue:

    def __init__(self):
        self.lis=[]

    def push(self, x: int) -> None:
        self.lis.append(x)

    def pop(self) -> int:
        x = self.lis[0]
        self.lis = self.lis[1:]
        return x
    
    def peek(self) -> int:
        return self.lis[0]

    def empty(self) -> bool:
        return len(self.lis)==0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()