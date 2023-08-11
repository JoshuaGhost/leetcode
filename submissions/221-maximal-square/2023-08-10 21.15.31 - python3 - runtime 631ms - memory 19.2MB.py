class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        max_square = [[0] * len(matrix[0]) for _ in matrix]
        res = 0
        for i, row in enumerate(matrix):
            if matrix[i][0] == '1':
                matrix[i][0] = 1
                res = 1
            else:
                matrix[i][0] = 0
            max_square[i][0] = row[0]
        for j, col in enumerate(matrix[0][1:], 1):
            if matrix[0][j] == '1':
                matrix[0][j] = 1
                res = 1
            else:
                matrix[0][j] = 0
            max_square[0][j] = matrix[0][j]
        for i, row in enumerate(matrix[1:], 1):
            for j, col in enumerate(row[1:], 1):
                if matrix[i][j] == '0':
                    matrix[i][j] = 0
                    continue
                matrix[i][j] = 1 + min(matrix[i - 1][j], matrix[i][j - 1])
                max_square[i][j] = min(max_square[i - 1][j - 1] + 1, matrix[i][j])
                res = max(res, max_square[i][j])
        return res ** 2
