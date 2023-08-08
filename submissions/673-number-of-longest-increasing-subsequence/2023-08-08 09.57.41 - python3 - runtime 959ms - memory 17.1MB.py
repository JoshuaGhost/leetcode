from collections import defaultdict


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = [(0, 0) for _ in nums]
        dp[0] = (1, 1)
        for i, n in enumerate(nums[1:], 1):
            max_len_to_count = defaultdict(int)
            for j, m in enumerate(nums[:i]):
                if n > m:
                    max_len_to_count[dp[j][0]] += dp[j][1]
            if len(max_len_to_count) == 0:
                dp[i] = (1, 1)
            else:
                max_len_to_count = sorted(
                    max_len_to_count.items(), key=lambda x: x[0], reverse=True
                )
                dp[i] = (max_len_to_count[0][0] + 1, max_len_to_count[0][1])
        max_len_to_count = defaultdict(int)
        for seq_len, cnt in dp:
            max_len_to_count[seq_len] += cnt
        max_len_to_count = sorted(
            max_len_to_count.items(), key=lambda x: x[0], reverse=True
        )
        return max_len_to_count[0][1]