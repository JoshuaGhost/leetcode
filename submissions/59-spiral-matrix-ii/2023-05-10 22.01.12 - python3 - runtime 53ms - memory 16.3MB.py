class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ret = [[0] * n for _ in range(n)]
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        p = 1
        for i in range(n // 2):
            coor = [i, i]
            for edge in range(4):
                for j in range(n - 2 * i - 1):
                    ret[coor[0]][coor[1]] = p
                    coor = [coor[0] + directions[edge][0], coor[1] + directions[edge][1]]
                    p += 1
        if p == n ** 2:
            ret[n // 2][n // 2] = p
        return ret