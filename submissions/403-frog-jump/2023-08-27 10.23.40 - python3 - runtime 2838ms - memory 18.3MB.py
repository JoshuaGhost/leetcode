class Solution:
    def canCross(self, stones: List[int]) -> bool:
        dp = [{}, {1} if stones[1] == 1 else {}]
        for i, s in enumerate(stones[2:], 2):
            dp.append(set())
            for j, ps in enumerate(stones[:i]):
                k = s - ps
                if k not in dp[-1] and (k in dp[j] or k - 1 in dp[j] or k + 1 in dp[j]):
                    dp[-1].add(k)
        return bool(dp[-1])