class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        sorted_candies = sorted(enumerate(candies), key=lambda x: x[1])
        p = 0
        while p < len(sorted_candies) and sorted_candies[p][1] < sorted_candies[-1][1] - extraCandies:
            p += 1
        res = [False] * len(candies)
        for idx, _ in sorted_candies[p:]:
            res[idx] = True
        return res