class Solution:
    memory = {}

    def min_layer(self, s: tuple) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        if s in self.memory:
            return self.memory[s]
        ret = int(1e200)
        for i, c in enumerate(s[:-1]):
            if c == s[-1]:
                temp = self.min_layer(s[: i + 1]) + self.min_layer(s[i + 1 : -1])
                ret = min(ret, temp)
        ret = min(self.min_layer(s[:-1]) + 1, ret)
        self.memory[s] = ret
        return ret

    def strangePrinter(self, s: str) -> int:
        s = list(s)
        st = 0
        for (
            i,
            c,
        ) in enumerate(s[1:], 1):
            if c != s[st]:
                st += 1
                s[st] = c
        s = tuple(s[: (st + 1)])
        return self.min_layer(s)