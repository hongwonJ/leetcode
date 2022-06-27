import heapq as hq

class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        n = len(sticks)
        costSum = 0
        
        hq.heapify(sticks)
        
        for _ in range(n-1):
            x = hq.heappop(sticks)
            y = hq.heappop(sticks)
            hq.heappush(sticks, x+y)
            costSum += (x + y)
        
        return costSum
      