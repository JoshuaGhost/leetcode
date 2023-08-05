class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] <= 0:
                nums[r], nums[l] = nums[l], nums[r]
                r -= 1
            else:
                l += 1
        
        for i, n in enumerate(nums[:l]):
            if abs(n) - 1 < l and nums[abs(n) - 1] > 0:
                nums[abs(n) - 1] = -nums[abs(n) - 1]

        for i in range(l):
            if nums[i] > 0:
                return i + 1
        return l + 1