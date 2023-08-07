class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        MODULO = int(1e9) + 7
        dp = [[0] * n for _ in range(goal)]
        dp[0][0] = n
        for t in range(1, goal):
            for i in range(n):
                dp[t][i] = dp[t - 1][i] * max(min(t, n, i + 1) - k, 0)
                if i > 0:
                    dp[t][i] += dp[t - 1][i - 1] * (n - i)
                dp[t][i] = dp[t][i] % MODULO
        return dp[goal - 1][n - 1]