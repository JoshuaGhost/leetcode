class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        def kmp_preprocess(s):
            ret = [0]
            p = 0
            for c in s[1:]:
                while p and s[p] != c:
                    p = ret[p - 1]
                if s[p] == c:
                    p += 1
                ret.append(p)
            return ret

        prefix = kmp_preprocess(s)
        return 2 * prefix[-1] >= len(s) and len(s) % (len(s) - prefix[-1]) == 0