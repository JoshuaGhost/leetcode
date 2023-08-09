class Solution:
    def largestVariance(self, s: str) -> int:
        def search_max_var(large_c, little_c):
            p = 0
            while s[p] != large_c and s[p] != little_c:
                p += 1
            n_large = [1 if s[p] == large_c else 0]
            n_little = [1 if s[p] == little_c else 0]
            values = [-1 if s[p] == little_c else 1]
            for idx, c in enumerate(s[p + 1 :], p + 1):
                if c == large_c:
                    if values[-1] + 1 >= 1:
                        values.append(values[-1] + 1)
                        n_large.append(n_large[-1] + 1)
                        n_little.append(n_little[-1])
                    else:
                        values.append(1)
                        n_large.append(1)
                        n_little.append(0)
                elif c == little_c:
                    if values[-1] - 1 > -1:
                        values.append(values[-1] - 1)
                        n_large.append(n_large[-1])
                        n_little.append(n_little[-1] + 1)
                    else:
                        values.append(-1)
                        n_large.append(0)
                        n_little.append(1)
            res = 0
            for a, b in zip(n_large, n_little):
                if b != 0:
                    res = max(res, a - b)
            return res

        res = 0
        for c1 in set(s):
            for c2 in set(s):
                if c1 == c2:
                    continue
                res = max(search_max_var(c1, c2), res)
                s = s[::-1]
                res = max(search_max_var(c1, c2), res)
                s = s[::-1]
        return res