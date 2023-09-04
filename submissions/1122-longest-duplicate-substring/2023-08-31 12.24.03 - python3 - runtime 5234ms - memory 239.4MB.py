class Solution:
    def longestDupSubstring(self, s: str) -> str:
        def duplicate(len_):
            coll = set()
            for i in range(len(s) - len_ + 1):
                if s[i: i + len_] in coll:
                    return i
                coll.add(s[i: i + len_])
            return None
        l, r = 0, len(s)
        ans = 0
        while l + 1 < r:
            mid = (l + r) // 2
            idx = duplicate(mid)
            if idx is not None:
                l = mid
                ans = idx
            else:
                r = mid
            
        return s[ans: ans + l]