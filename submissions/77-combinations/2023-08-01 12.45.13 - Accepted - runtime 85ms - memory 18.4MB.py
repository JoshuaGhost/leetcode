class Solution:
    def _combine(self, bitmap: int, k: int, last_bit_pos: int) -> List[int]:
        if self.n - last_bit_pos < k:
            return None
        if k == 0:
            return [bitmap]
        if self.n - last_bit_pos == k:
            for t in range(last_bit_pos, self.n):
                bitmap |= 1 << t
            return [bitmap]
        st = last_bit_pos
        ret = []
        for i in range(st, self.n - k + 1):
            r = self._combine(bitmap | (1 << i), k - 1, i + 1)
            if r is not None:
                ret += r
        return ret

    def decode(self, bitmap: int) -> List[int]:
        ret = []
        for p in range(self.n - 1, -1, -1):
            if bitmap & 1 << p:
                ret.append(p + 1)
        return ret

    def combine(self, n: int, k: int) -> List[List[int]]:
        self.n = n
        return [self.decode(b) for b in self._combine(0, k, 0)]