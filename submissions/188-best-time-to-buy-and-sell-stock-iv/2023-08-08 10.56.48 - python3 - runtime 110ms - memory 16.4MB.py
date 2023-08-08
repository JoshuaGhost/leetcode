class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        dp = (
            [[float("-inf"), 0]]
            + [[-prices[0], float("-inf")]]
            + [[float("-inf"), float("-inf")] for _ in range(k - 1)]
        )
        for i, p in enumerate(prices[1:], 1):
            for t in range(k, 0, -1):
                dp[t][1] = max(dp[t][1], dp[t][0] + p)
                dp[t][0] = max(dp[t - 1][1] - p, dp[t][0])
        return max([_[1] for _ in dp])