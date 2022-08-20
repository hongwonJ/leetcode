class MinStack:

    def __init__(self):
        self.stack = []
        self.min = float('inf')

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val < self.min: self.min = val

    def pop(self) -> None:
        x = self.stack.pop()
        if not self.stack:
            self.min = float('inf')
        if x == self.min:
            self.min = min(self.stack)
            

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        if self.min == float('inf'): return None
        return self.min
        
        
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()