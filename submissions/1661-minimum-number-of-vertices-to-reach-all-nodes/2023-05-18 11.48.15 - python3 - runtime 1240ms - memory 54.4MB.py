class Solution:    
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        u, v = list(map(set, zip(*edges)))
        return list(u.difference(v))