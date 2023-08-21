import bisect

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs = sorted(pairs, key=lambda x: (x[0], -x[1]))
        min_right = []
        for l, r in pairs:
            p = bisect.bisect_left(min_right, l)
            if p == len(min_right):
                min_right.append(r)
            else:
                min_right[p] = min(r, min_right[p])
        return len(min_right)