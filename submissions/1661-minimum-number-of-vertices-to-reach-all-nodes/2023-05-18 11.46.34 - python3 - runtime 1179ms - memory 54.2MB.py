class Solution:    
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        distinct_res = set(range(n))
        for u, v in edges:
            if v in distinct_res:
                distinct_res.remove(v)
        return list(distinct_res)