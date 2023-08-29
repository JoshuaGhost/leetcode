import bisect

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        if len(intervals) == 1:
            if intervals[0][0] == intervals[0][1]:
                return [0]
            return [-1]

        intervals = sorted(zip(intervals, range(len(intervals))))
        ret = [-1] * len(intervals)
        for (st, ed), i in intervals:
            p = bisect.bisect_left(intervals, ed, key=lambda x: x[0][0])
            ret[i] = intervals[p][1] if p < len(intervals) else -1
        return ret
            