class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        profit_total = sum(profit)
        a = [[0 for j in range(n + 1)] for i in range(profit_total)]
        a = [[1] + [0] * n] + a
        count = [1] + [0] * profit_total
        for crime_size, crime_profit in zip(group, profit):
            for i in range(profit_total, -1, -1):
                if count[i] > 0:
                    for base_size in range(n - crime_size, -1, -1):
                        a[i + crime_profit][base_size + crime_size] += a[i][base_size]
                        count[i + crime_profit] += a[i][base_size]

        return sum([_ for _ in count[minProfit:]]) % int(1000000007)