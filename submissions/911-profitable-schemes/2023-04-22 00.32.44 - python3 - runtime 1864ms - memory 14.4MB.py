class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        a = [[0 for j in range(n + 1)] for i in range(minProfit)]
        a = [[1] + [0] * n] + a
        for crime_size, crime_profit in zip(group, profit):
            for i in range(minProfit, -1, -1):
                for size in range(n, crime_size - 1, -1):
                    a[i][size] += a[max(0, i - crime_profit)][size - crime_size] % int(1000000007)

        return sum(a[minProfit]) % int(1000000007)