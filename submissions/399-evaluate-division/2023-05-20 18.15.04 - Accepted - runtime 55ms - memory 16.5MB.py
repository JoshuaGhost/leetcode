from itertools import chain

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def dfs(p, q, temp):
            if p == q:
                return temp
            if visit[p]:
                return -1
            visit[p] = True
            for i in range(len(vocab)):
                if a[p][i] > 0:
                    r = dfs(i, q, temp * a[p][i])
                    if r > 0:
                        return r
            return -1

        vocab = sorted(set(chain.from_iterable(equations)))
        a = [[0] * len(vocab) for _ in vocab]
        for (x_char, y_char), v in zip(equations, values):
            x = vocab.index(x_char)
            y = vocab.index(y_char)
            a[x][x] = 1.
            a[y][y] = 1.
            a[x][y] = v
            a[y][x] = 1/v
        from pprint import pprint
        pprint(a)
        ret = []
        visited = []
        for x_char, y_char in queries:
            if x_char not in vocab or y_char not in vocab:
                ret.append(-1)
                continue
            x = vocab.index(x_char)
            y = vocab.index(y_char)
            visit = [False] * len(vocab)
            res = dfs(x, y, 1)
            ret.append(res)
        return ret