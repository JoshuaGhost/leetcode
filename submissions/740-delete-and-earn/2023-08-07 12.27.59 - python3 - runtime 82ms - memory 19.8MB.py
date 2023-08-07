from collections import Counter

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        nums = sorted(list(Counter(nums).items()), key = lambda x: x[0])
        nums = [[n[0], n[1] * n[0]] for n in nums]
        if len(nums) == 1:
            return nums[0][1]
        if len(nums) == 2:
            if nums[0][0] == nums[1][0] - 1:
                return max(nums[0][1], nums[1][1])
            return nums[0][1] + nums[1][1]
        ps = [[0, 0] for _ in nums]
        for i, (n, s) in enumerate(nums):
            ps[i][0] = max(ps[i - 1][1], ps[i-1][0])
            if n == nums[i - 1][0] + 1:
                ps[i][1] = max(ps[i - 1][0], ps[i-2][1]) + s
            else:
                ps[i][1] = ps[i][0] + s
        return max(ps[-1])