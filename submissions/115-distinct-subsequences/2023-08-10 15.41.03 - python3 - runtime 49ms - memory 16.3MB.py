class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        dp = [1] + [0] * len(t)
        for i in range(n - m + 1):
            for j in range(m):
                if t[j] == s[i + j]:
                    dp[j + 1] += dp[j]
        return dp[-1]