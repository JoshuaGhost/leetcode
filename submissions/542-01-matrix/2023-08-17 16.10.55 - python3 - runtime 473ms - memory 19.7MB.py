from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        def new_dirs(i, j):
            if i > 0:
                yield i - 1, j
            if i < m - 1:
                yield i + 1, j
            if j > 0:
                yield i, j - 1
            if j < n - 1:
                yield i, j + 1

        m = len(mat)
        n = len(mat[0])
        inf = m * n + 1
        ret = [[inf] * n for _ in range(m)]
        visit = deque()
        for i, row in enumerate(mat):
            for j, ele in enumerate(row):
                if ele == 0:
                    ret[i][j] = 0
                elif ((i > 0 and mat[i - 1][j] == 0) or 
                (i < m - 1 and mat[i + 1][j] == 0) or
                (j > 0 and mat[i][j - 1] == 0) or
                (j < n - 1 and mat[i][j + 1] == 0)) and ret[i][j] == inf:
                    ret[i][j] = 1
                    visit.append((i, j))
        while visit:
            i, j = visit.popleft()
            for x, y in new_dirs(i, j):
                if ret[x][y] == inf:
                    ret[x][y] = ret[i][j] + 1
                    visit.append((x, y))
        return ret      