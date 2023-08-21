from collections import deque
import bisect

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        w = deque()
        p = deque()
        res = []
        for i, n in enumerate(nums):
            pos = bisect.bisect(w, n)
            for _ in range(pos):
                w.popleft()
                p.popleft()
            w.appendleft(nums[i])
            p.appendleft(i)
            if i >= k - 1:
                res.append(w[-1])
            if p[-1] <= i - k + 1:
                w.pop()
                p.pop()
        return res
