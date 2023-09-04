class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def _path(v):
            if v == n - 1:
                return [[v]]
            ret = []
            for u in graph[v]:
                ret += [[v] + p for p in _path(u)]
            return ret
        n = len(graph)
        return _path(0)