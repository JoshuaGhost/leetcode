class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 1:
            return triangle[0][0]
        res = [triangle[0][0]] + [float("inf")] * len(triangle)
        for row_idx, row in enumerate(triangle[1:], 1):
            res[len(row) - 1] = res[len(row) - 2] + row[-1]
            for col_idx in range(len(row) - 2, 0, -1):
                element = row[col_idx]
                res[col_idx] = element + min(res[col_idx - 1], res[col_idx])
            res[0] = res[0] + row[0]
        return min(res)