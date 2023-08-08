class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for i, line in enumerate(grid):
            for j, element in enumerate(line):
                if i == 0 and j == 0:
                    continue
                min_score = 1e100
                if i != 0:
                    min_score = min(min_score, grid[i - 1][j] + grid[i][j])
                if j != 0:
                    min_score = min(min_score, grid[i][j - 1] + grid[i][j])
                grid[i][j] = min_score
        return grid[-1][-1]