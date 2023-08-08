import bisect

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events = sorted(events, key=lambda x: x[0])
        dp = {}

        def search(idx, k):
            if dp.get((idx, k), None) is not None:
                return dp[(idx, k)]
            if k == 0:
                return 0
            if idx >= len(events):
                return 0
            st, ed, v = events[idx]
            next_idx = bisect.bisect_right(events, ed, key=lambda x: x[0])
            select_current = v + search(next_idx, k - 1)
            skip_current = search(idx + 1, k)
            dp[(idx, k)] = max(select_current, skip_current)
            return dp[(idx, k)]

        return search(0, k)