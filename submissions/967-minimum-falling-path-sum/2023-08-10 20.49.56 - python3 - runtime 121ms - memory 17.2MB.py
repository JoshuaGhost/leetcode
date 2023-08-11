class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        if len(matrix[0]) == 1:
            return sum(r[0] for r in matrix)
        for i, row in enumerate(matrix[1:], 1):
            matrix[i][0] = row[0] + min(matrix[i - 1][0], matrix[i - 1][1])
            matrix[i][-1] = row[-1] + min(matrix[i - 1][-1], matrix[i - 1][-2])
            for j, element in enumerate(row[1: -1], 1):
                matrix[i][j] = element + min(
                    matrix[i - 1][j],
                    matrix[i - 1][j - 1],
                    matrix[i - 1][j + 1],
                )
        return min(matrix[-1])