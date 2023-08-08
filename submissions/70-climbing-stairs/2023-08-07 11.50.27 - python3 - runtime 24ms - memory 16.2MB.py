@cache
def fac(i: int) -> int:
    if i == 0 or i == 1:
        return 1
    return i * fac(i - 1)

@cache
def c(a, b):
    return fac(a)//(fac(b) * fac(a-b))

class Solution:
    def climbStairs(self, n: int) -> int:
        num_two_max = n // 2
        ret = 0
        for num_two in range(num_two_max + 1):
            num_one = n - num_two * 2
            ret += c(num_two + num_one, min(num_one, num_two))
        return ret
