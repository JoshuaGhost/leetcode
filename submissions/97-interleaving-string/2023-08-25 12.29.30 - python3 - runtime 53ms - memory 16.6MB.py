class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if s2 == "":
            return s1 == s3
        elif s1 == "":
            return s2 == s3
        if len(s1) + len(s2) != len(s3):
            return False
        dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        dp[0][0] = True
        for j, c2 in enumerate(s2, 1):
            dp[0][j] = dp[0][j - 1] and s3[j - 1] == c2
        for i, c1 in enumerate(s1, 1):
            dp[i][0] = dp[i - 1][0] and s3[i - 1] == c1
            for j, c2 in enumerate(s2, 1):
                c3 = s3[i + j - 1]
                if c3 == c1:
                    dp[i][j] |= dp[i - 1][j]
                if c3 == c2:
                    dp[i][j] |= dp[i][j - 1]
        return dp[-1][-1]