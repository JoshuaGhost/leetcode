import math
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MODULO = int(1e9 + 7)
        res = [1] + [0] * high
        for i in range(high):
            if i + zero <= high:
                res[i + zero] += res[i] % MODULO
            if i + one <= high:
                res[i + one] += res[i] % MODULO
        return sum(res[low: high + 1]) % MODULO