import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        rec = []
        for n in nums:
            p = bisect.bisect_left(rec, n)
            if p == len(rec):
                rec.append(n)
            else:
                rec[p] = n
        return len(rec)