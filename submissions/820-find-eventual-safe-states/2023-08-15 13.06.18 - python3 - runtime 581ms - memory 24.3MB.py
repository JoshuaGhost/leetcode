class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        terms = set()
        visit = [False] * len(graph)
        for idx, conn in enumerate(graph):
            if len(conn) == 0:
                terms.add(idx)
                visit[idx] = True

        def on_loop(p):
            visit[p] = True
            for v in graph[p]:
                if v in terms:
                    continue
                if not visit[v]:
                    ret = on_loop(v)
                    if ret:
                        return True
                else:
                    return True
            terms.add(p)
            return False

        for v in range(len(graph)):
            if not visit[v]:
                on_loop(v)
        return sorted(terms)