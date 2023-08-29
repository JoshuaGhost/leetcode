class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        end_red = [9999] * n
        red_edges = [[9999] * n for _ in range(n)]
        for u, v in redEdges:
            if u == 0:
                end_red[v] = 1
            red_edges[u][v] = 1
        end_red[0] = 0

        end_blue = [9999] * n
        blue_edges = [[9999] * n for _ in range(n)]
        for u, v in blueEdges:
            if u == 0:
                end_blue[v] = 1
            blue_edges[u][v] = 1
        end_blue[0] = 0

        visit_end_blue = [False] * n
        visit_end_red = [False] * n
        visit_end_blue[0] = True
        visit_end_red[0] = True
        for _ in range(n):
            min_end_blue, min_end_blue_v = 9999, 0
            for v, l in enumerate(end_blue[1:], 1):
                if min_end_blue > l and not visit_end_blue[v]:
                    min_end_blue = l
                    min_end_blue_v = v
            v = min_end_blue_v
            visit_end_blue[v] = True
            for u in range(n):
                end_red[u] = min(end_red[u], min_end_blue + red_edges[v][u])

            min_end_red, min_end_red_v = 9999, 0
            for v, l in enumerate(end_red[1:], 1):
                if min_end_red > l and not visit_end_red[v]:
                    min_end_red = l
                    min_end_red_v = v
            v = min_end_red_v
            visit_end_red[v] = True
            for u in range(n):
                end_blue[u] = min(end_blue[u], min_end_red + blue_edges[v][u])

        ret = [min(r, b) if min(r, b) <  9999 else -1 for r, b in zip(end_red, end_blue)]
        ret[0] = 0
        return ret