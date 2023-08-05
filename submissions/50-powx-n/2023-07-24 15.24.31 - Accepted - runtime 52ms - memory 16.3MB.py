class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n < 0:
            return 1/self.myPow(x, -n)
        if x == 1:
            return 1
        if n == 0:
            return 1
        if n == 1:
            return x
        r = self.myPow(x, n // 2)
        if n % 2 == 1:
            return r * r * x
        else:
            return r * r