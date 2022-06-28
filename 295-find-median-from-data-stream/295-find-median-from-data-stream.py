import heapq

class MedianFinder:

    def __init__(self):
        # 최대값 heap, 저장개수는 n//2
        self.L = []
        # 최소값 heap, 저장개수는 n//2
        self.R = []
        self.isEven = True

    def addNum(self, num: int) -> None:
        self.isEven = not self.isEven
        
        if not self.L:
            self.L.append(-num)
            return
       
        if self.isEven:
            if -self.L[0] <= num:
                heapq.heappush(self.R, num)
            else: 
                tmp = -heapq.heappop(self.L)
                heapq.heappush(self.R, tmp)
                heapq.heappush(self.L, -num)
        else:
            if num <= self.R[0]: heapq.heappush(self.L, -num)
            else:
                tmp = heapq.heappop(self.R)
                heapq.heappush(self.L, -tmp)
                heapq.heappush(self.R, num)
            
        
        return

    def findMedian(self) -> float:
        if self.isEven: return (-self.L[0] + self.R[0])/2
        else: return -self.L[0]
            

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()