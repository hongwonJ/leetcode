from collections import deque
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = {i:[] for i in range(n)}
        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)

        que = deque([source])
        seen = set([source])
        while que: 
            k = len(que)
            for _ in range(k):
                curr = que.popleft()
                if curr == destination:
                    return True
                for adj in graph[curr]:
                    if adj not in seen:
                        seen.add(adj)
                        que.append(adj)
        return False


