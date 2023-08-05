class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        a = [0] * len(s) + [1]
        from math import ceil, log
        k_len = ceil(log(k)/log(10))
        for fast, fast_c in enumerate(s):
            for slow, slow_c in enumerate(s[max(fast - k_len + 1, 0): fast + 1], max(fast - k_len + 1, 0)):
                if slow_c == '0':
                    continue
                if int(s[slow: fast + 1]) <= k:
                    a[fast] += a[slow - 1] % 1000000007
        return a[len(s) - 1] % 1000000007