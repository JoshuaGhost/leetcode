class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        inf = max(amount * 2 // min(coins), 999)
        dp = [inf] * (amount + 1)
        dp[0] = 0
        for c in coins:
            for i in range(amount + 1):
                if i + c <= amount:
                    dp[i + c] = min(dp[i + c], dp[i] + 1)
        return dp[-1] if dp[-1] != inf else -1