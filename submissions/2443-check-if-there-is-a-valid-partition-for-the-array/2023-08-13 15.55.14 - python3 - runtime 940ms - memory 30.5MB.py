class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return False
        dp = [True, False, nums[0] == nums[1]]
        p = dp[-1]
        for i, n in enumerate(nums[2:], 2):
            p = (n == nums[i - 1]) & (dp[-2])
            p = p | (n == nums[i - 1]) & (nums[i - 1] == nums[i - 2]) & dp[-3]
            p = p | (n == nums[i - 1] + 1) & (nums[i - 1] == nums[i - 2] + 1) & dp[-3]
            dp = dp[1], dp[2], p
        return p