class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1
        dp = [1] + [0] * amount
        for c in coins:
            for i in range(amount + 1):
                if i + c <= amount:
                    dp[i + c] += dp[i]
        return dp[-1]