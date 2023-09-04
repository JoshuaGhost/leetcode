class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0] * (len(days) + 1)
        for idx, day in enumerate(days, 1):
            dp[idx] = min(
                dp[bisect.bisect(days, day - d, 0, idx - 1)] + c
                for d, c in zip((1, 7, 30), costs)
            )
        return dp[-1]