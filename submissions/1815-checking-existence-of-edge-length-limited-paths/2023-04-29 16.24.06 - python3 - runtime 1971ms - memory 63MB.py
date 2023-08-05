class DS:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def combine(self, a, b):
        root_a = self.find_root(a)
        root_b = self.find_root(b)
        if self.rank[root_a] < self.rank[root_b]:
            self.parent[root_a] = root_b
        else:
            self.parent[root_b] = root_a
        if self.rank[root_a] == self.rank[root_b]:
            self.rank[root_a] += 1

    def find_root(self, v):
        if self.parent[v] == v:
            return v
        self.parent[v] = self.find_root(self.parent[v])
        return self.parent[v]

    def have_same_root(self, a, b):
        return self.find_root(a) == self.find_root(b)


class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        sorted_queries = sorted(enumerate(queries), key = lambda x: x[1][2])
        sorted_edges = sorted(edgeList, key=lambda x: x[2])
        res = [False] * len(queries)
        eid_offset = 0
        ds = DS(n)
        for orig_i, (p, q, lim) in sorted_queries:
            # don't do this, this leads to double-check to each sorted_edges[eid_offset]-s,
            # which results in doubling the steps in extreme situation
            # for eid, (u, v, l) in enumerate(sorted_edges[eid_offset:], eid_offset):
            #     if l >= lim:
            #         eid_offset = eid
            #         break
            #     ds.combine(u, v)

            while eid_offset < len(sorted_edges) and sorted_edges[eid_offset][2] < lim:
                ds.combine(sorted_edges[eid_offset][0], sorted_edges[eid_offset][1])
                eid_offset += 1
            res[orig_i] = ds.have_same_root(p, q)
        return res