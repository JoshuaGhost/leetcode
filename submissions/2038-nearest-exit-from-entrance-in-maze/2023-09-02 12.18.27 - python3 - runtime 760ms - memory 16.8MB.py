from collections import deque


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        n, m = len(maze), len(maze[0])
        q = deque([entrance + [0]])
        visited = [[False] * m for _ in maze]
        visited[entrance[0]][entrance[1]] = True
        while q:
            r, c, t = q.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m and maze[nr][nc] != '+' and not visited[nr][nc]:
                    if (nr == 0 or nr == n - 1 or nc == 0 or nc == m - 1):
                        return t + 1
                    q.append((nr, nc, t + 1))
                    visited[nr][nc] = True
        return -1