class Solution:
    def numSquares(self, n: int) -> int:
        sqrtn = int(n ** 0.5) + 1
        if n % sqrtn == 0 and n // sqrtn == sqrtn:
            return 1
        dp = [999] * (n + 1)
        dp[0] = 0
        for sqrte in range(sqrtn, 0, -1):
            ele = sqrte ** 2
            for i in range(n + 1):
                if i + ele <= n and dp[i] + 1 < dp[i + ele]:
                    dp[i + ele] = dp[i] + 1
        return dp[-1]
