from collections import deque

class Solution:    
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        prev = [None] * len(edges)
        other = [None] * len(edges)
        last = [None] * n
        self.distinct_res = set(range(n))
        for idx, (u, v) in enumerate(edges):
            prev[idx] = last[u]
            last[u] = idx
            other[idx] = v
        for u in range(n):
            if u not in self.distinct_res:
                continue
            dq = deque([u])
            while dq:
                u = dq.popleft()
                idx = last[u]
                while idx is not None:
                    v = other[idx]
                    if v in self.distinct_res:
                        dq.append(v)
                        self.distinct_res.discard(v)
                    idx = prev[idx]
        return list(self.distinct_res)