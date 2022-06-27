import heapq as hq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        for point in points:
            point.insert(0, point[0]**2+point[1]**2)
        ans = []
        hq.heapify(points)
        for _ in range(k):
            x = hq.heappop(points)
            ans.append(x[1:])
        
        return ans
        