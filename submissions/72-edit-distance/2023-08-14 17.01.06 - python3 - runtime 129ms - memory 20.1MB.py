class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) == 0:
            return len(word2)
        if len(word2) == 0:
            return len(word1)
        dis = [[0] * (len(word2)+1) for _ in range(len(word1) + 1)]
        dis[0][0] = 0
        for j in range(1, len(word2) + 1):
            dis[0][j] = j
        for i in range(1, len(word1) + 1):
            dis[i][0] = i
        for i, c1 in enumerate(word1, 1):
            for j, c2 in enumerate(word2, 1):
                dis[i][j] = min(
                    dis[i - 1][j - 1] + (1 if c1 != c2 else 0),
                    dis[i - 1][j] + 1,
                    dis[i][j - 1] + 1
                )
        return dis[-1][-1]