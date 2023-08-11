class Solution:
    @cache
    def numDistinct(self, s: str, t: str) -> int:
        if len(t) == 0:
            return 1
        if len(s) == 0:
            return 0
        ret = 0
        if t[-1] == s[-1]:
            ret += self.numDistinct(s[:-1], t[:-1])
        ret += self.numDistinct(s[:-1], t)
        return ret