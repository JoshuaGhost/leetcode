from itertools import product
from collections import deque
from typing import List
from copy import deepcopy


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        def bfs(i, j):
            res = 40000
            dist = [[40000] * len(line) for line in grid]
            dist[i][j] = 0
            q = deque([(i, j)])
            while q:
                i, j = q.popleft()
                if grid[i][j] == 0:
                    cost = 1
                else:
                    cost = 0
                for di, dj in dirs:
                    if not(0 <= i + di < len(grid) and 0 <= j + dj < len(grid[0])):
                        continue
                    if dist[i + di][j + dj] <= dist[i][j] + cost:
                        continue
                    dist[i + di][j + dj] = dist[i][j] + cost
                    q.append((i + di, j + dj))
            for i, line in enumerate(grid):
                for j, c in enumerate(line):
                    if c == 1 and dist[i][j] != 0:
                        res = min(res, dist[i][j])
            return res

        for i, line in enumerate(grid):
            for j, c in enumerate(line):
                if grid[i][j] == 1:
                    return bfs(i, j)