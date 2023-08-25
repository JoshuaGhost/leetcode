import bisect

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        s = bisect.bisect(grid[0], 0, key= lambda x: -x)
        res = 0
        for i, row in enumerate(grid):
            j = s - 1
            for j in range(s - 1, -1, -1):
                if row[j] >= 0:
                    break
            s = j + 1
            res += (m - j - 1) if row[j] >= 0 else m
        return res