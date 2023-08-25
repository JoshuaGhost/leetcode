from collections import defaultdict

class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = [defaultdict(int) for _ in nums]
        res = 1
        for i, n in enumerate(nums[1:], 1):
            for j, m in enumerate(nums[:i]):
                dp[i][n - m] = dp[j][n - m] + 1
                res = max(dp[i][n - m], res)
        return res + 1