class Solution:
    def convert_abs_to_xy(self, _abs):
        return _abs // self.shape[1], _abs % self.shape[1]
    def search(self, st, ed, t):
        if st > ed:
            return False
        xst, yst = self.convert_abs_to_xy(st)
        xed, yed = self.convert_abs_to_xy(ed)
        if st == ed:
            return xst < self.shape[0] and yst < self.shape[1] and self.matrix[xst][yst] == t
        mid = (st + ed)//2
        xmid, ymid = self.convert_abs_to_xy(mid)
        if self.matrix[xmid][ymid] > t:
            return self.search(st, mid, t)
        elif self.matrix[xmid][ymid] < t:
            return self.search(mid + 1, ed, t)
        else:
            return True

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        self.matrix = matrix
        self.shape = len(matrix), len(matrix[0])
        if self.shape[0] == 1:
            return target in self.matrix[0]
        return self.search(0, self.shape[0] * self.shape[1], target)
