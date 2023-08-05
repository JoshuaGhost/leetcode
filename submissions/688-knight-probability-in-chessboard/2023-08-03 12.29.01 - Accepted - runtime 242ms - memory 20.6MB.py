class Solution:
    dirs = [(-1, -2), (-2, -1), (1, -2), (2, -1), (-1, 2), (-2, 1), (1, 2), (2, 1)]
    def get_num_on_board(self, k, r, c) -> int:
        if not (0 <= r < self.n and 0 <= c < self.n):
            return 0
        if k == 0:
            return 1
        if (k, r, c) in self.rec:
            return self.rec[(k, r, c)]
        ret = 0.
        for dr, dc in self.dirs:
            ret +=  0.125 * self.get_num_on_board(k - 1, r + dr, c + dc)
        self.rec[(k, r, c)] = ret
        return ret

    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        self.rec = {}
        if k == 0:
            return 1.0
        self.n = n
        return self.get_num_on_board(k, row, column)