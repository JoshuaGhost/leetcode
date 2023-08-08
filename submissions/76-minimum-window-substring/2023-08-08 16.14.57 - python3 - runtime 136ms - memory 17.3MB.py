from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        len_t = len(t)
        cur_len = 0
        t = Counter(t)
        now = {k: 0 for k in t}
        st, ed = -1, -1
        res = ""
        while ed < len(s) - 1:
            while cur_len < len_t and ed < len(s) - 1:
                ed += 1
                ced = s[ed]
                if ced in t:
                    if now[ced] < t[ced]:
                        cur_len += 1
                    now[ced] += 1
            while cur_len == len_t and st <= ed:
                if ed - st < len(res) or res == "":
                    res = s[st + 1 : ed + 1]
                st += 1
                cst = s[st]
                if cst in t:
                    now[cst] -= 1
                    if now[cst] < t[cst]:
                        cur_len -= 1
        return res
