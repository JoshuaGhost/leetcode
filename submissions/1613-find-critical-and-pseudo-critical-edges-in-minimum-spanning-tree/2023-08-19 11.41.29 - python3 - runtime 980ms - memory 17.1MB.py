class Solution:
    def findCriticalAndPseudoCriticalEdges(
        self, n: int, edges: List[List[int]]
    ) -> List[List[int]]:
        def mst(n, block=None, use=None):
            def ancestor(v):
                if p[v] == v:
                    return v
                p[v] = ancestor(p[v])
                return p[v]

            p = list(range(n))
            ret = 0
            if use is not None:
                _, (u, v, w) = edges[use]
                p[u] = v
                ret += w
            for i, (_, (u, v, w)) in enumerate(edges):
                if block is not None and i == block:
                    continue
                pu = ancestor(u)
                pv = ancestor(v)
                if pu != pv:
                    p[pu] = pv
                    ret += w
            p_res = -1
            for v in range(n):
                if p_res == -1:
                    p_res = ancestor(v)
                elif ancestor(v) != p_res:
                    return float('inf')
            return ret

        edges = list(enumerate(edges))
        edges = sorted(edges, key=lambda x: x[1][2])
        base_weight = mst(n, edges)
        critical = []
        pseudo = []
        for i, (idx, _) in enumerate(edges):
            mst_weight = mst(n, block=i)
            if mst_weight > base_weight:
                critical.append(idx)
            else:
                mst_weight = mst(n, use=i)
                if mst_weight == base_weight:
                    pseudo.append(idx)
        return critical, pseudo