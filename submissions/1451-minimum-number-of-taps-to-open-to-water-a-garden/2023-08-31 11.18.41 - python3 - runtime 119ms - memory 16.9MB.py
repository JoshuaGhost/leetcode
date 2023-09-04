import bisect

class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        right_most_from = [-1] * (n + 1) 
        for i, l in enumerate(ranges):
            if l == 0:
                continue
            left = max(0, i - l)
            right = min(i + l, n)
            right_most_from[left] = max(right_most_from[left], right)
        right_most, ret, candidate = 0, 0, 0
        for i, right in enumerate(right_most_from):
            if i > right_most:
                if candidate <= right_most:
                    return -1
                right_most = candidate
                ret += 1
            candidate = max(right, candidate)
        return ret