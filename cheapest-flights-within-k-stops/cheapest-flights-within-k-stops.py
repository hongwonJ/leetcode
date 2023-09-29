class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prev =  [float('inf') if i != src else 0 for i in range(n)]
        curr = prev.copy()
        
        indeg = {i:[] for i in range(n)}
        for s, e, p in flights:
            indeg[e].append((s, p))
        for i in range(k+1):
            for j in range(n):
                for s, p in indeg[j]:

                    curr[j] = min(prev[j], prev[s]+p, curr[j])
            prev = curr.copy()
        return curr[dst] if curr[dst] < float('inf') else -1
