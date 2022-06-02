class MyQueue:

    def __init__(self):
        self.A = []
        self.size = 0

    def push(self, x: int) -> None:
        self.A.append(x)
        self.size += 1
        
    def pop(self) -> int:
        if self.empty(): return None
        
        tmp = []
        while self.A:
            tmp.append(self.A.pop())
        top = tmp.pop()
        while tmp:
            self.A.append(tmp.pop())
        self.size -= 1
        return top
       
    def peek(self) -> int:
        if self.empty(): return None
        else: return self.A[0]
        
    def empty(self) -> bool:
        if self.size == 0: return True
        else: return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()