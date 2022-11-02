import heapq as hq

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        n = len(boxTypes)
        stored_heap = []
        hq.heapify(stored_heap)
        empty_space = truckSize
        total_weight = 0
        
        
        for i in range(n):
            for j in range(boxTypes[i][0]):
                units =	boxTypes[i][1]
                if empty_space > 0:
                    hq.heappush(stored_heap, units)
                    empty_space -= 1
                    total_weight += units            
                else:
                    if units > stored_heap[0]:
                        total_weight += units - stored_heap[0]  
                        hq.heappush(stored_heap,units)
                        hq.heappop(stored_heap)
        
        return total_weight
        

        