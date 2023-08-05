class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        def dfs(p, c):
            if color[p] != 0:
                return color[p] == c
            color[p] = c
            for n in graph[p]:
                if not dfs(n, -c):
                    return False
            return True

        color = [0] * len(graph)
        for start_node in range(len(graph)):
            if color[start_node] == 0:
                if not dfs(start_node, 1):
                    return False
        return True