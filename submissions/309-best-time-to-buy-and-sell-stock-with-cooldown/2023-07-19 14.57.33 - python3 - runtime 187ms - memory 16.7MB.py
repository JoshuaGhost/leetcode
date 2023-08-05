class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        buy = [-prices[0]]
        cool, sell = 0, 0
        for price in prices[1:]:
            buy.append(cool - price)
            cool = max(cool, sell)
            sell = price + max(buy[:-1])
        return max(sell, cool)