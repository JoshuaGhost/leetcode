class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[float('-inf'), 0], [-prices[0], float('-inf')], [float('-inf'), float('-inf')]]
        for p in prices[1:]:
            for t in range(2, 0, -1):
                dp[t][1] = max(dp[t][1], dp[t][0] + p)
                dp[t][0] = max(dp[t][0], dp[t - 1][1] - p)
        return max(max([_[1] for _ in dp]), 0)