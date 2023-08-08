class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 2:
            return min(cost)
        pay = [0] + cost[:2] + [1e100] * (len(cost) - 1)
        cost += [0]
        for i in range(3, len(cost) + 1):
            pay[i] = cost[i - 1] + min(pay[i - 2: i])
        return pay[-1]