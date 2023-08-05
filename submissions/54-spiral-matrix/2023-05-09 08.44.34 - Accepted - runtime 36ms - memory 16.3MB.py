from math import ceil


class Solution:
    def get_shape(self, matrix: List[List[int]]) -> Tuple[int]:
        m = len(matrix)
        if m == 0:
            return (0, 0)
        n = len(matrix[0])
        return (m, n)
    def get_outer_ring(self, matrix: List[List[int]]) -> List[int]:
        m, n = self.get_shape(matrix)
        if m == 0 or n == 0:
            return []
        if n == 1 or m == 1:
            return list(chain.from_iterable(matrix))
        return matrix[0][:-1] + \
              [_[n-1] for _ in matrix[:-1]] + \
              matrix[m - 1][:0:-1] + \
              [_[0] for _ in matrix][:0:-1]
    
    def inner(self, matrix: List[List[int]]) -> List[int]:
        m, n = self.get_shape(matrix)
        return [[j for j in line[1: -1]] for line in matrix[1: -1]]
    
    def recursive_get(self, matrix):
        m, n = self.get_shape(matrix)
        if n == 1 or m == 1 or n == 0 or m == 0:
            return self.get_outer_ring(matrix)
        return self.get_outer_ring(matrix) + self.recursive_get(self.inner(matrix))
        
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        return self.recursive_get(matrix)