class Solution:
    def count_connected_components(self, a: List[List[int]]) -> int:
        def flood_fill(a, n, b):
            for other_n in range(len(a)):
                if not b[other_n] and a[n][other_n] == 1:
                    b[other_n] = True
                    flood_fill(a, other_n, b)

        b = [False] * len(a)
        res = 0
        for n in range(len(a)):
            if not b[n]:
                res += 1
                flood_fill(a, n, b)
        return res

    def similar(self, s0, s1) -> bool:        
        if len(s0) != len(s1):
            return False
        
        if s0 == s1:
            return True

        diffs = []
        for c0, c1 in zip(s0, s1):
            if c0 != c1:
                diffs.append(ord(c0) - ord(c1))
    
        if len(diffs) != 2:
            return False

        if sum(diffs) != 0:
            return False
        
        return True            

    def numSimilarGroups(self, strs: List[str]) -> int:
        a = [[0] * len(strs) for _ in strs]
        for i in range(len(strs)):
            a[i][i] = 1
        for idx0, s0 in enumerate(strs[1:], 1):
            for idx1, s1 in enumerate(strs[:idx0]):
                if self.similar(s0, s1):
                    a[idx0][idx1] = 1
                    a[idx1][idx0] = 1

        return self.count_connected_components(a)