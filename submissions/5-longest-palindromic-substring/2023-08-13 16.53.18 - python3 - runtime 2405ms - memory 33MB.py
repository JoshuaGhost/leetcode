class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[0] * (len(s) + 1) for _ in range(len(s) + 1)]
        ret_i = 1
        ret_j = 0
        for i, c in enumerate(s, 1):
            dp[i - 1][i] = 1
            for j in range(i - 2, -1, -1):
                if s[i - 1] == s[j] and dp[j + 1][i - 1] == i - j - 2:
                    dp[j][i] = dp[j + 1][i - 1] + 2
                    if dp[j][i] > dp[ret_j][ret_i]:
                        ret_j, ret_i = j, i
        return s[ret_j:ret_i]