class Solution:
    memory = {}
    def min_layer(self, s: tuple) -> int:
        print(s)
        if len(s) == 1:
            return 1
        if s in self.memory:
            return self.memory[s]
        ret = int(1e200)
        for i, c in enumerate(s):
            if i != 0 and i != len(s) - 1 and s[i-1] == s[i + 1]:
                temp_s = s[:i] + s[i + 2:]
            else:
                temp_s = s[:i] + s[i + 1:]
            ret = min(ret, self.min_layer(temp_s))
        ret += 1
        self.memory[s] = ret
        return ret

    def strangePrinter(self, s: str) -> int:
        s = list(s)
        st = 0
        for i, c, in enumerate(s[1:], 1):
            if c != s[st]:
                st += 1
                s[st] = c
        s = tuple(s[:(st + 1)])

        return self.min_layer(s)