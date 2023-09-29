class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths, path = [], [0]
        que = collections.deque([[0]])
        seen = set([0])
        while que:
            k = len(que)
            for _ in range(k):
                path_so_far = que.popleft()
                curr = path_so_far[-1]
                for adj in graph[curr]:
                    new_path = path_so_far[:]
                    new_path.append(adj)
                    if adj == len(graph)-1:
                        paths.append(new_path[:])
                    que.append(new_path)

        return paths