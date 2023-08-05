from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        sorted_counter = sorted(c.items(), key=lambda x: x[1], reverse=True)
        return [_[0] for _ in sorted_counter[:k]]