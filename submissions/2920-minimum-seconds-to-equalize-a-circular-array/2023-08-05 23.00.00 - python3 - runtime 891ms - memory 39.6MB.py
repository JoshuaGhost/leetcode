from typing import List


class Solution:
    def minimumSeconds(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        temp = sorted(enumerate(nums), key=lambda x: x[1] * len(nums) + x[0])
        head = 1
        tail = 0
        min_gap = int(1e9)
        while head < n:
            max_gap = 0
            while head < n and temp[head][1] == temp[tail][1]:
                gap = temp[head][0] - temp[head - 1][0]
                max_gap = max(max_gap, gap)
                head += 1
            max_gap = max(max_gap, temp[tail][0] + n - temp[head - 1][0])
            min_gap = min(min_gap, max_gap)
            tail = head
        return min_gap // 2
