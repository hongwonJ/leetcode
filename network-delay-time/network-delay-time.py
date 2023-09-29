class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {i:[] for i in range(1, n+1)}

        for s, e, d in times:
            graph[s].append((e,d))
        
        dists = [float('inf') if i != k else 0 for i in range(n+1)]
        visited = set()
        not_visited = set([i for i in range(1, n+1)])
        stack = [k]
        while stack:
            curr = stack.pop()
            visited.add(curr)
            not_visited.remove(curr)
            min_dist = float('inf')
            for adj, dist in graph[curr]:
                dists[adj] = min(dists[adj], dist + dists[curr])
            next_dist = float('inf')
            next_node = None
            for nxt in not_visited:
                if dists[nxt] < next_dist:
                    next_node = nxt
                    next_dist = dists[nxt]
            if next_node is not None:
                stack.append(next_node)

        max_dist = max(dists[1:])

        if len(visited) == n and max_dist < float('inf'):
            return max_dist
        return -1

        
            

                



