class Solution:
    def cumsum(self, s: str):
        ret = 0
        for c in s:
            ret += ord(c)
        return ret

    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        score = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        for p1 in range(1, len(s1) + 1):
            score[p1][0] = self.cumsum(s1[:p1])
        for p2 in range(1, len(s2) + 1):
            score[0][p2] = self.cumsum(s2[:p2])
        for p1 in range(1, len(s1) + 1):
            c1 = s1[p1 - 1]
            for p2 in range(1, len(s2) + 1):
                c2 = s2[p2 - 1]
                if c1 == c2:
                    score[p1][p2] = score[p1 - 1][p2 - 1]
                else:
                    score[p1][p2] = min(
                        ord(c2) + score[p1][p2 - 1], ord(c1) + score[p1 - 1][p2]
                    )
        return score[len(s1)][len(s2)]
