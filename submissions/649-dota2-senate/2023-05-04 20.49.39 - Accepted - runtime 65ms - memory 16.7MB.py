from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        lr, ld = deque(), deque()
        n = len(senate)
        for idx, c in enumerate(senate):
            if c == "R":
                lr.append(idx)
            else:
                ld.append(idx)
        
        while lr and ld:
            r, d = lr.popleft(), ld.popleft()
            if r < d:
                lr.append(r + n)
            else:
                ld.append(d + n)
        return "Dire" if len(lr) == 0 else "Radiant"
