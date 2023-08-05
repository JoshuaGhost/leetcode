class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        ret = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n):
            ret[i][i + 1] = 1

        for length in range(2, n + 1):
            for left in range(n - length + 1):
                right = left + length
                ret[left][right] = max(
                    ret[left][right],
                    ret[left + 1][right],
                    ret[left][right - 1]
                )
                if s[left] == s[right - 1]:
                    ret[left][right] = max(
                        ret[left][right],
                        ret[left + 1][right - 1] + 2
                    )
        return ret[0][n]