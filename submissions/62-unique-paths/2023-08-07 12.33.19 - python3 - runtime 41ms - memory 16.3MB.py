@cache
def fac(i):
    if i in (0, 1):
        return 1
    return i * fac(i - 1)
def c(a, b):
    return fac(a) // (fac(b) * fac(a - b))
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return c(m + n - 2, min(m - 1, n - 1))