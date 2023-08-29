import heapq

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        buy, sell = -prices[0] - fee, 0
        for p in prices[1:]:
            buy = max(buy, sell - p - fee)
            sell = max(sell, buy + p)
        return sell