class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        for i, line in enumerate(obstacleGrid):
            for j, element in enumerate(line):
                if element == 1:
                    obstacleGrid[i][j] = -1
                    continue
                if i == 0 and j == 0:
                    obstacleGrid[i][j] = 1
                    continue                
                if i != 0:
                    obstacleGrid[i][j] += obstacleGrid[i - 1][j] if obstacleGrid[i - 1][j] != -1 else 0
                if j != 0:
                    obstacleGrid[i][j] += obstacleGrid[i][j - 1] if obstacleGrid[i][j - 1] != -1 else 0
        return max(obstacleGrid[-1][-1], 0)
