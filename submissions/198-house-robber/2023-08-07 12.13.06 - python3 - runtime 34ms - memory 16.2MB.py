class Solution:
    def rob(self, nums: List[int]) -> int:
        r = [[0, 0] for i in nums]
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        for i, m in enumerate(nums):
            r[i][0] = max(r[i - 1][1], r[i - 1][0])
            r[i][1] = max(r[i - 1][0], r[i - 2][1]) + m
        return max(r[-1])