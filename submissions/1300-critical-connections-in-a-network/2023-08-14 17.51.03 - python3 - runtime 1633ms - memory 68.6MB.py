class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        c = [[] for _ in range(n)]
        for u, v in connections:
            c[u].append(v)
            c[v].append(u)
        low = [n] * n
        critical = []
        def dfs(cur_node, time, in_node):
            if low[cur_node] != n:
                return low[cur_node]
        
            low[cur_node] = time
            for v in c[cur_node]:
                if v == in_node:
                    continue

                out_time = dfs(v, time + 1, cur_node)
                if out_time >= time + 1:
                    critical.append((cur_node, v))
                low[cur_node] = min(low[cur_node], out_time)
            return low[cur_node]
        dfs(0, 0, -1)
        return critical