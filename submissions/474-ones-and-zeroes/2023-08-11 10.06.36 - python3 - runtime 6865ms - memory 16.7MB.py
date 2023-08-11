from collections import Counter

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        strs = [Counter(s) for s in strs]
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        ret = 0
        for s in strs:
            for i in range(m, -1, -1):
                for j in range(n, -1, -1):
                    if i + s['0'] <= m and j + s['1'] <= n:
                        dp[i + s['0']][j + s['1']] = max(dp[i][j] + 1, dp[i + s['0']][j + s['1']])
                        ret = max(ret, dp[i + s['0']][j + s['1']])
        return ret