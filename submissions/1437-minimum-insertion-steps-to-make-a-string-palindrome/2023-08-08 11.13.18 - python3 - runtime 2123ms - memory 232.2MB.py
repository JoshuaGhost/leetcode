class Solution:
    @cache
    def min_intersections(self, st, ed):
        if st == ed - 1 or st == ed:
            return 0
        ret = min(
            self.min_intersections(st, ed - 1) + 1,
            self.min_intersections(st + 1, ed) + 1
        )
        if self.s[st] == self.s[ed - 1]:
            ret = min(
                self.min_intersections(st + 1, ed - 1), 
                ret
            )
        return ret

    def minInsertions(self, s: str) -> int:
        self.s = s
        return self.min_intersections(0, len(s))