class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        res = [[0] * (len(words[0]) + 1) for _ in range(len(target) + 1)]
        MODULO = int(1e9 + 7)
        for c_idx, c in enumerate(target, 1):
            for p in range(c_idx, len(words[0]) + 1 - (len(target) - c_idx)):
                counter = 0
                for w in words:
                    if w[p - 1] == c:
                        counter += 1
                if c_idx == 1:
                    res[c_idx][p] = counter
                else:
                    s = sum(res[c_idx - 1][c_idx - 1: p])
                    res[c_idx][p] = (counter * s) % MODULO
        return sum(res[len(target)]) % MODULO