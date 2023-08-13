from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = defaultdict(int)
        p = -1
        if len(s) <= 1:
            return len(s)
        res = 1
        for i, c in enumerate(s):
            if d[c] == 0:
                d[c] += 1
                res = max(i - p, res)
                continue
            d[c] += 1
            res = max(i - p - 1, res)
            while d[c] > 1 and p < i:
                p += 1
                d[s[p]] -= 1
            res = max(i - p, res)
        return res