class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * len(text2) for _ in text1]
        for i, c1 in enumerate(text1):
            for j, c2 in enumerate(text2):
                if c1 == c2:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    if i != 0 and j != 0:
                        dp[i][j] = dp[i - 1][j - 1]
                    if i != 0:
                        dp[i][j] = max(dp[i][j], dp[i - 1][j])
                    if j != 0:
                        dp[i][j] = max(dp[i][j], dp[i][j - 1])
        return dp[-1][-1]