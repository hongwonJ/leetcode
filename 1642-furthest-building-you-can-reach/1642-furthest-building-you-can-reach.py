import heapq as hq

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        gap = []
        
        for i in range(n-1):
            if heights[i] < heights[i+1]:
                gap.append([heights[i+1]-heights[i], i+1])
        
        heap, used_bricks = [], 0
        last = -1
        
        for i in range(len(gap)):
            if i < ladders:
                hq.heappush(heap, gap[i])
                last = i
                continue
            if heap and gap[i] > heap[0]: x = heappushpop(heap, gap[i])
            else: x = gap[i]
            if used_bricks + x[0] <= bricks: 
                used_bricks += x[0]
                last = i
            else: break
        
        return gap[last+1][1]-1 if last < len(gap)-1 else len(heights) - 1
     
        