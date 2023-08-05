class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        sums = list(map(sum, mat))
        sorted_sums = sorted(enumerate(sums), key=lambda x: x[1])
        return [_[0] for _ in sorted_sums[:k]]