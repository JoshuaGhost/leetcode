class Solution:
    def numTilings(self, n: int) -> int:
        modulo = int(10 ** 9 + 7)
        dp = [[1, 0, 0], [2, 1, 1]]
        if n <= 2:
            return dp[n - 1][0]
        for i in range(2, n):
            dp.append([
                (dp[i-1][0] + dp[i - 2][0] + dp[i - 1][1] + dp[i - 1][2]) % modulo,
                (dp[i - 2][0] + dp[i - 1][2]) % modulo,
                (dp[i - 2][0] + dp[i - 1][1]) % modulo
                ])
        return dp[-1][0]
        