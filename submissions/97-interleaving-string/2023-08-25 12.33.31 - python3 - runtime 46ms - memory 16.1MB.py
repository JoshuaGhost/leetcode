class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        dp = [True] + [False] * len(s2)
        for j, c2 in enumerate(s2, 1):
            dp[j] = dp[j - 1] and s3[j - 1] == c2
        for i, c1 in enumerate(s1, 1):
            dp[0] &= s3[i - 1] == c1
            for j, c2 in enumerate(s2, 1):
                c3 = s3[i + j - 1]
                dp[j] = (dp[j] and c3 == c1) or (dp[j-1] and c3 == c2)
        return dp[-1]