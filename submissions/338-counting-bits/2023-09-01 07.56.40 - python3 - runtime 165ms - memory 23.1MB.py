class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n + 1):
            res.append(0)
            while i > 0:
                res[-1] += i % 2
                i //= 2
        return res 