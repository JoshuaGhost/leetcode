class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [1] + [0] * len(s)
        for i, c in enumerate(s, 1):
            dp[i] = dp[i - 1] if c != "0" else 0
            if i <= 1:
                continue
            if (ord(s[i - 2]) - ord("0")) * 10 + ord(c) - ord("0") <= 26 and s[i - 2] != '0':
                dp[i] += dp[i - 2]
        return dp[-1]