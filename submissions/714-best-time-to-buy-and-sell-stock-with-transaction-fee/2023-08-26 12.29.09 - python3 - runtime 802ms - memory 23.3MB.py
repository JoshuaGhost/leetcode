import heapq

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        heap = []
        last = 0
        for p in prices:
            heapq.heappush(heap, -(last - p))
            hist = -heapq.heappop(heap)
            heapq.heappush(heap, -hist)
            last = max(last,  hist - fee + p)
        return last