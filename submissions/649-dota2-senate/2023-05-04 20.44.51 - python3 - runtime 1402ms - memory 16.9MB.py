class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        lr, ld = [], []
        n = len(senate)
        for idx, c in enumerate(senate):
            if c == "R":
                lr.append(idx)
            else:
                ld.append(idx)
        
        while len(lr) != 0 and len(ld) != 0:
            if lr[0] < ld[0]:
                lr = lr[1:] + [lr[0] + n]
                ld = ld[1:]
            else:
                ld = ld[1:] + [ld[0] + n]
                lr = lr[1:]
        return "Dire" if len(lr) == 0 else "Radiant"
            