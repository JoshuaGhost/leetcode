class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dp = [len(s) + 1]*(len(s) + 1)
        dp[0] = 0
        for i, c in enumerate(s, 0):
            if i > 0:
                dp[i] = min(dp[i - 1] + 1, dp[i])
            for word in dictionary:
                if s[i:].startswith(word):
                    dp[i + len(word)] = min(dp[i], dp[i + len(word)])
        dp[-1] = min(dp[-2] + 1, dp[-1])
        return dp[-1]