import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = nums[:k]
        heapq.heapify(h)
        for n in nums[k:]:
            if n > h[0]:
                heapq.heappop(h)
                heapq.heappush(h, n)
        return h[0]