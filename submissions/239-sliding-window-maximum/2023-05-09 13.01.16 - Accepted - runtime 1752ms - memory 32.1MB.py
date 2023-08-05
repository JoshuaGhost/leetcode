from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        ret = []
        for idx, n in enumerate(nums):
            if dq and dq[0][0] <= idx - k:
                dq.popleft()
            while dq and dq[-1][1] < n:
                dq.pop()
            dq.append((idx, n))
            if idx >= k - 1:
                ret.append(dq[0][1])
        return ret