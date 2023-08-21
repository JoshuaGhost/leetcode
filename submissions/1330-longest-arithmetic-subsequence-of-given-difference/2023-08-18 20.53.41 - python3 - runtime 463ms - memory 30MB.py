from collections import defaultdict

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = defaultdict(int)
        ret = 0
        for n in arr:
            dp[n] = dp[n - difference] + 1
            ret = max(ret, dp[n])
        return ret

