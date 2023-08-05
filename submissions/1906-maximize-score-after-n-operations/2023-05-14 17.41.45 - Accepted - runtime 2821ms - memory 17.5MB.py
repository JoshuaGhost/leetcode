import math
class Solution:
    def gcd(self, a, b) -> int:
        if (a, b) in self.gcd_cache:
            return self.gcd_cache[(a, b)]
        if (b, a) in self.gcd_cache:
            return self.gcd_cache[(b, a)]
        self.gcd_cache[(a, b)] = math.gcd(a, b)
        self.gcd_cache[(b, a)] = self.gcd_cache[(a, b)]
        return self.gcd_cache[(a, b)]

    def search(self, r, bitmask) -> int:
        if r == self.n + 1:
            return 0
        if bitmask in self.res_cache:
            return self.res_cache[bitmask]
        for idx1, n1 in enumerate(self.nums):
            if (1 << idx1) & bitmask:
                continue
            for idx2, n2 in enumerate(self.nums[idx1 + 1:], idx1 + 1):
                if (1 << idx2) & bitmask:
                    continue
                self.res_cache[bitmask] = max(self.res_cache.get(bitmask, 0),
                                           r * self.gcd(n1, n2) + self.search(r + 1,
                                                                              bitmask | (1 << idx1) | (1 << idx2)))
        return self.res_cache[bitmask]

    def maxScore(self, nums: List[int]) -> int:
        self.n = len(nums) // 2
        self.nums = nums
        self.gcd_cache = dict()
        self.res_cache = dict()
        return self.search(1, 0)