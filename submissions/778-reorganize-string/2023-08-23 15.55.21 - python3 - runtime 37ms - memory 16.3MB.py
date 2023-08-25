from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        sc = Counter(s)
        sc = sorted(sc.items(), key=lambda x: x[1], reverse=True)
        if sc[0][1] > (len(s) + 1) // 2:
            return ''
        ret = [0] * len(s)
        p = 0
        for c, count in sc:
            for _ in range(count):
                if p >= len(s):
                    p = 1
                ret[p] = c
                p += 2
        return ''.join(ret)
