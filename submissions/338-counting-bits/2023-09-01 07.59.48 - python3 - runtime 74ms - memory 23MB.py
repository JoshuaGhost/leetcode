class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0, 1]
        for i in range(2, n + 1):
            res.append(res[(i >> 1)] + i % 2)
        return res[: n + 1]