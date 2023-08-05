class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: x[1])
        prev_idx = 0
        removed = 0
        for idx, (st, ed) in enumerate(intervals[1:], 1):
            if st >= intervals[prev_idx][1]:
                prev_idx = idx
            else:
                removed += 1
        return removed