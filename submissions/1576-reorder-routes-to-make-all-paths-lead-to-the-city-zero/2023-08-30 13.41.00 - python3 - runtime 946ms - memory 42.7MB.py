from collections import deque
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        edges, rev_edges = defaultdict(list), defaultdict(list)
        for u, v in connections:
            edges[u].append(v)
            rev_edges[v].append(u)

        q = deque([0])
        visited = [False] * n
        visited[0] = True
        ret = 0
        while q:
            p = q.popleft()
            for v in edges[p]:
                if visited[v]:
                    continue
                q.append(v)
                ret += 1
                visited[v] = True
            for v in rev_edges[p]:
                if visited[v]:
                    continue
                q.append(v)
                visited[v] = True
        return ret