import bisect

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes = sorted(envelopes, key=lambda x: (x[0], -x[1]))
        res = []
        for _, h in envelopes:
            p = bisect.bisect_left(res, h)
            if p == len(res):
                res.append(h)
            else:
                res[p] = h
        return len(res)