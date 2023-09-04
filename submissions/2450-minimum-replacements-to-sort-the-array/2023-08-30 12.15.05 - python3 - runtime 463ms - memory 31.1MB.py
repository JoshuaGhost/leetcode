class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        ret = 0
        prev = inf
        for n in reversed(nums):
            t = 1 if n <= prev else n // prev + int(n % prev != 0)
            prev = n // t
            ret += t
        return ret - len(nums)