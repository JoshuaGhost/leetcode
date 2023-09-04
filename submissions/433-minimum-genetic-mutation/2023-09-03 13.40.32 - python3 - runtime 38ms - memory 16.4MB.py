from collections import deque

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        def diff(g1, g2):
            ret = 0
            for c1, c2 in zip(g1, g2):
                ret += c1 != c2
            return ret

        if endGene not in bank:
            return -1
            
        bank = bank if startGene in bank else bank + [startGene]
        a = [[False] * len(bank) for _ in bank]
        for i, g1 in enumerate(bank):
            for j, g2 in enumerate(bank):
                if i != j and diff(g1, g2) == 1:
                    a[i][j] = True
        
        target = bank.index(endGene)
        q = deque([(bank.index(startGene), 0)])

        visited = [False] * len(bank)
        visited[bank.index(startGene)] = True
        while q:
            p, t = q.popleft()
            for v, e in enumerate(a[p]):
                if e and not visited[v]:
                    if v == target:
                        return t + 1
                    else:
                        visited[v] = True
                        q.append((v, t + 1))
        return -1