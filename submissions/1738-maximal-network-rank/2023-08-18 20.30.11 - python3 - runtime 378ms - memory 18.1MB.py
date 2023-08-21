from collections import defaultdict

class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        rev_roads = [[v, u] for u, v in roads]
        r = defaultdict(list)
        for u, v in roads:
            if u in r:
                r[u].append(v)
            else:
                r[u] = [v]
            if v in r:
                r[v].append(u)
            else:
                r[v] = [u]
        ret = 0
        for u in range(n):
            for v in range(n):
                if u == v:
                    continue
                t = len(r[u]) + len(r[v])
                if u in r[v]:
                    t -= 1
                ret = max(t, ret)
        return ret